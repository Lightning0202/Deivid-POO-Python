import tkinter as tk
from tkinter import messagebox

class Pokemon:
    def __init__(self, vida, ataque, defensa, tipo):
        self._vida = 0
        self._ataque = ataque
        self._defensa = defensa
        self._tipo = tipo
        self.vida = vida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nueva_vida):
        self._vida = max(0, min(500, nueva_vida))

    @property
    def ataque(self):
        return self._ataque

    @property
    def defensa(self):
        return self._defensa

    @property
    def tipo(self):
        return self._tipo

    def calcular_efectividad(self, tipo_objetivo):
        ventajas = {
            'fuego': 'planta',
            'agua': 'fuego',
            'planta': 'agua'
        }
        if ventajas.get(self.tipo) == tipo_objetivo:
            return 2.0
        elif ventajas.get(tipo_objetivo) == self.tipo:
            return 0.5
        else:
            return 1.0


class Charizard(Pokemon):
    def __init__(self):
        super().__init__(vida=230, ataque=60, defensa=50, tipo="fuego")

    def ataques(self):
        return [("Llamarada", self.llamarada), ("Fuego Fatuo", self.fuego_fatuo)]

    def llamarada(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 1.5 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        return f"Llamarada causó {daño:.2f} de daño."

    def fuego_fatuo(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 0.8 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        objetivo._defensa = max(0, objetivo.defensa - 5)
        return f"Fuego Fatuo causó {daño:.2f} de daño y bajó la defensa del oponente."


class Blastoise(Pokemon):
    def __init__(self):
        super().__init__(vida=250, ataque=55, defensa=40, tipo="agua")

    def ataques(self):
        return [("Hidrobomba", self.hidrobomba), ("Aqua Jet", self.aqua_jet)]

    def hidrobomba(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 2 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        return f"Hidrobomba causó {daño:.2f} de daño."

    def aqua_jet(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 0.8 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        return f"Aqua Jet causó {daño:.2f} de daño."


class Torterra(Pokemon):
    def __init__(self):
        super().__init__(vida=235, ataque=60, defensa=50, tipo="planta")

    def ataques(self):
        return [("Hoja Afilada", self.hoja_afilada), ("Bomba Germen", self.bomba_germen)]

    def hoja_afilada(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 1.2 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        return f"Hoja Afilada causó {daño:.2f} de daño."

    def bomba_germen(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = max(0, (self.ataque * 0.9 - objetivo.defensa) * efectividad)
        objetivo.vida -= daño
        mensaje = f"Bomba Germen causó {daño:.2f} de daño."
        if objetivo.tipo != "planta":
            objetivo.vida -= 5
            mensaje += f" ¡Y envenenó al rival! -5 vida adicional."
        return mensaje


# ---------- Interfaz con Tkinter ----------
class JuegoPokemon:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalla Pokémon")
        self.jugador1 = None
        self.jugador2 = None
        self.turno = 1
        self.seleccionar_pokemon()

    def seleccionar_pokemon(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Jugador 1: Elige tu Pokémon").pack()

        for nombre, clase in [("Charizard", Charizard), ("Blastoise", Blastoise), ("Torterra", Torterra)]:
            tk.Button(self.root, text=nombre, command=lambda c=clase: self.set_jugador1(c)).pack(pady=2)

    def set_jugador1(self, clase):
        self.jugador1 = clase()
        self.limpiar_ventana()
        tk.Label(self.root, text="Jugador 2: Elige tu Pokémon").pack()

        for nombre, clase in [("Charizard", Charizard), ("Blastoise", Blastoise), ("Torterra", Torterra)]:
            tk.Button(self.root, text=nombre, command=lambda c=clase: self.set_jugador2(c)).pack(pady=2)

    def set_jugador2(self, clase):
        self.jugador2 = clase()
        self.batalla()

    def batalla(self):
        self.limpiar_ventana()

        self.estado = tk.Label(self.root, text="", justify="left")
        self.estado.pack(pady=10)

        self.boton_ataques = []
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        self.estado.config(text=f"Jugador 1: {self.jugador1.__class__.__name__} (Vida: {self.jugador1.vida:.2f})\n"
                                f"Jugador 2: {self.jugador2.__class__.__name__} (Vida: {self.jugador2.vida:.2f})\n"
                                f"Turno de Jugador {self.turno}")

        for b in self.boton_ataques:
            b.destroy()
        self.boton_ataques.clear()

        jugador = self.jugador1 if self.turno == 1 else self.jugador2
        rival = self.jugador2 if self.turno == 1 else self.jugador1

        for nombre_ataque, funcion in jugador.ataques():
            boton = tk.Button(self.root, text=nombre_ataque,
                              command=lambda f=funcion: self.ejecutar_ataque(f, jugador, rival))
            boton.pack(pady=2)
            self.boton_ataques.append(boton)

    def ejecutar_ataque(self, ataque_func, atacante, defensor):
        mensaje = ataque_func(defensor)
        mensaje_final = f"{atacante.__class__.__name__} atacó a {defensor.__class__.__name__}.\n{mensaje}"

        if defensor.vida <= 0:
            messagebox.showinfo("¡Fin del juego!", f"{defensor.__class__.__name__} fue derrotado.\n{mensaje_final}")
            self.root.destroy()
        else:
            self.turno = 2 if self.turno == 1 else 1
            self.actualizar_interfaz()
            self.estado.config(text=self.estado.cget("text") + "\n\n" + mensaje_final)

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------- Ejecutar la ventana ----------
if __name__ == "__main__":
    ventana = tk.Tk()
    app = JuegoPokemon(ventana)
    ventana.mainloop()
