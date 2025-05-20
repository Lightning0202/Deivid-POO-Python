import pygame
import random
import time

# Inicializamos el mezclador de pygame para música
pygame.mixer.init()

# Reproducir música de fondo
def reproducir_musica():
    pygame.mixer.music.load("C:\\Users\\deivi\\Music\\pokemon\\PokemonIntro.mp3")  # Asegúrate de poner la ruta correcta de tu archivo de música
                                                                                    #se utilizo doble \\ ya que con uno solo daba error por alguna razon
    pygame.mixer.music.play(-1)  # El -1 indica que la música se repetirá indefinidamente

# Llamamos a la función de música
reproducir_musica()

class Pokemon:
    def __init__(self, vida, ataque, defensa, tipo):
        self._vida = 0
        self._ataque = ataque
        self._defensa = defensa
        self._tipo = tipo
        self.vida = vida  # Usa el setter que valida

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, nueva_vida):
        if nueva_vida < 0:
            self._vida = 0
        elif nueva_vida > 100:
            self._vida = 100
        else:
            self._vida = nueva_vida

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, nuevo_ataque):
        self._ataque = nuevo_ataque

    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, nueva_defensa):
        self._defensa = nueva_defensa

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def atacar(self, objetivo):
        efectividad = self.calcular_efectividad(objetivo.tipo)
        daño = (self.ataque - objetivo.defensa) * efectividad
        daño = max(0, daño)  # No puede ser daño negativo
        objetivo.vida -= daño
        print(f"{self.tipo} ataca a {objetivo.tipo}, causando {daño:.2f} de daño.")

    def calcular_efectividad(self, tipo_objetivo):
        # Simplificamos: solo 3 tipos para el ejemplo
        ventajas = {
            'fuego': 'planta',
            'agua': 'fuego',
            'planta': 'agua'
        }
        if ventajas.get(self.tipo) == tipo_objetivo:
            return 2.0  # Super efectivo
        elif ventajas.get(tipo_objetivo) == self.tipo:
            return 0.5  # Poco efectivo
        else:
            return 1.0  # Neutro



class Charizard(Pokemon):
    def atacar(self, objetivo):
        print(f"¡{self.__class__.__name__} va a atacar al {objetivo.__class__.__name__}!")
        print("Elige un ataque:")
        print("1. Llamarada (daño fuerte)")
        print("2. Fuego Fatuo (daño bajo + debilita la defensa del enemigo)")

        opcion = input("Selecciona el ataque (1 o 2): ")

        if opcion == "1":
            self.llamarada(objetivo)
        elif opcion == "2":
            self.fuego_fatuo(objetivo)
        else:
            print("Opción no válida. Charizard pierde su turno.")

    def llamarada(self, objetivo):
        print(f"{self.__class__.__name__} usa Llamarada 🔥!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 1.5  # 50% más fuerte
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)
        objetivo.vida -= daño
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Vida restante del objetivo: {objetivo.vida:.2f}")

    def fuego_fatuo(self, objetivo):
        print(f"{self.__class__.__name__} usa Fuego Fatuo 🔥👻!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 0.8  # 20% más débil que el ataque normal
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)  # Nunca puede ser negativo
        objetivo.vida -= daño
        objetivo.defensa = max(0, objetivo.defensa - 5)  # Baja la defensa del objetivo
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Defensa del objetivo reducida a {objetivo.defensa}.")
        print(f"Vida restante del objetivo: {objetivo.vida:.2f}")





class Blastoise(Pokemon):
    def atacar(self, objetivo):
        print(f"¡{self.__class__.__name__} va a atacar al {objetivo.__class__.__name__}!")
        print("Elige un ataque:")
        print("1. Hidrobomba (daño alto, menos preciso)")
        print("2. Aqua Jet (daño bajo, más rápido)")

        opcion = input("Selecciona el ataque (1 o 2): ")

        if opcion == "1":
            self.hidrobomba(objetivo)
        elif opcion == "2":
            self.aqua_jet(objetivo)
        else:
            print("Opción no válida. Blastoise pierde su turno.")

    def hidrobomba(self, objetivo):
        print(f"{self.__class__.__name__} usa Hidrobomba 💦!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 2  # Doble daño, pero menos preciso
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)
        objetivo.vida -= daño
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Vida restante del objetivo: {objetivo.vida:.2f}")

    def aqua_jet(self, objetivo):
        print(f"{self.__class__.__name__} usa Aqua Jet 💧!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 0.8  # Menos daño, pero más rápido
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)  # Nunca puede ser negativo
        objetivo.vida -= daño
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Vida restante del objetivo: {objetivo.vida:.2f}")



class Torterra(Pokemon):
    def atacar(self, objetivo):
        print(f"¡{self.__class__.__name__} va a atacar al {objetivo.__class__.__name__}!")
        print("Elige un ataque:")
        print("1. Hoja Afilada (daño moderado y precisión alta)")
        print("2. Bomba Germen (daño bajo, pero puede causar envenenamiento)")

        opcion = input("Selecciona el ataque (1 o 2): ")

        if opcion == "1":
            self.hoja_afilada(objetivo)
        elif opcion == "2":
            self.bomba_germen(objetivo)
        else:
            print("Opción no válida. Torterra pierde su turno.")

    def hoja_afilada(self, objetivo):
        print(f"{self.__class__.__name__} usa Hoja Afilada 🍃!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 1.2  # Daño moderado, alta precisión
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)
        objetivo.vida -= daño
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Vida restante del objetivo: {objetivo.vida:.2f}")

    def bomba_germen(self, objetivo):
        print(f"{self.__class__.__name__} usa Bomba Germen 🌱💥!")
        efectividad = self.calcular_efectividad(objetivo.tipo)
        ataque_mejorado = self.ataque * 0.9  # Menos daño, pero con efecto adicional
        daño = (ataque_mejorado - objetivo.defensa) * efectividad
        daño = max(0, daño)
        objetivo.vida -= daño
        # Añadir un efecto de envenenamiento
        if objetivo.tipo != 'planta':  # Suponiendo que las plantas no pueden ser envenenadas
            print(f"¡{objetivo.__class__.__name__} está envenenado!")
            # Envenenamiento: pierde vida en cada turno posterior
            objetivo.vida -= 5
            print(f"¡{objetivo.__class__.__name__} pierde 5 puntos de vida por envenenamiento!")
        print(f"Daño causado: {daño:.2f} (efectividad {efectividad}x). Vida restante del objetivo: {objetivo.vida:.2f}")





# Aquí debes definir las clases de los Pokémon (Charizard, Blastoise, Torterra, etc.)

def elegir_pokemon(jugador_numero):
    print(f"\nJugador {jugador_numero}, elige un Pokémon:")
    print("1. Charizard (Fuego)")
    print("2. Blastoise (Agua)")
    print("3. Torterra (Planta)")

    opcion = input("Selecciona el número de tu Pokémon (1, 2, o 3): ")

    if opcion == "1":
        return Charizard(vida=230, ataque=60, defensa=50, tipo="fuego")
    elif opcion == "2":
        return Blastoise(vida=250, ataque=55, defensa=40, tipo="agua")
    elif opcion == "3":
        return Torterra(vida=235, ataque=60, defensa=50, tipo="planta")
    else:
        print("Opción no válida, elige otra vez.")
        return elegir_pokemon(jugador_numero)

def batalla(jugador1, jugador2):
    print("\nLa batalla comienza!")
    
    # Determinar quién empieza primero
    primero = random.choice([jugador1, jugador2])
    segundo = jugador2 if primero == jugador1 else jugador1
    
    print(f"{primero.__class__.__name__} empieza primero!")
    
    while jugador1.vida > 0 and jugador2.vida > 0:
        # Turno del jugador 1
        print(f"\nTurno de {primero.__class__.__name__}:")
        primero.atacar(segundo)

        if segundo.vida <= 0:
            print(f"{segundo.__class__.__name__} ha sido derrotado!")
            break

        # Turno del jugador 2
        print(f"\nTurno de {segundo.__class__.__name__}:")
        segundo.atacar(primero)

        if primero.vida <= 0:
            print(f"{primero.__class__.__name__} ha sido derrotado!")
            break

def menu():
    print("Bienvenido al juego de batalla Pokémon!")
    
    jugador1 = elegir_pokemon(1)
    jugador2 = elegir_pokemon(2)

    batalla(jugador1, jugador2)

# Ejecutar el menú
menu()
