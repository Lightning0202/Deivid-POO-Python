
import tkinter as tk
from tkinter import messagebox, simpledialog
from textblob import TextBlob  

# Dato de opiniones en global donde se guardara todas las opiniones
opiniones = []

# Clase padre Restaurante 
class Restaurante:
    def __init__(self, nombre, categoria, horario, menu):
        self.nombre = nombre
        self.categoria = categoria
        self.horario = horario
        self.menu = menu

# Clases hijas
class BurgerKing(Restaurante):
    def __init__(self):
        menu = {
            "Whopper": 6.49,
            "Papas Fritas": 2.79,
            "Onion Rings": 3.19
        }
        super().__init__("Burger King", "Comida rápida", "9:00 AM - 10:00 PM", menu)

class McDonalds(Restaurante):
    def __init__(self):
        menu = {
            "Big Mac": 5.99,
            "McNuggets": 4.49,
            "Papas Fritas": 2.99
        }
        super().__init__("McDonald's", "Comida rápida", "8:00 AM - 11:00 PM", menu)

class PizzaHut(Restaurante):
    def __init__(self):
        menu = {
            "Pizza Suprema": 8.99,
            "Pizza Pepperoni": 7.99,
            "Pan de Ajo": 3.49
        }
        super().__init__("Pizza Hut", "Pizzería", "10:00 AM - 11:00 PM", menu)

class SalvatorePizza(Restaurante):
    def __init__(self):
        menu = {
            "Pizza Margarita": 9.49,
            "Lasagna": 7.49,
            "Tiramisú": 4.99
        }
        super().__init__("Salvatore Pizza", "Pizzería Italiana", "11:00 AM - 9:00 PM", menu)

# Función para analizar el sentimiento de una opinión
def analizar_sentimiento(texto):
    texto_original = texto.lower()  # Convertir texto a minúsculas para mejor análisis
    traducciones = {
        "me gusto": "I liked it",
        "no me gusto": "I didn't like it",
        "no me gustó": "I didn't like it",
        "pésimo": "awful",
        "horrible": "horrible",
        "excelente": "excellent",
        "delicioso": "delicious",
        "rico": "tasty",
        "malo": "bad",
        "bueno": "good",
        "regular": "average"
    }

    # Traducir palabras clave al inglés para que TextBlob las entienda mejor
    for palabra, reemplazo in traducciones.items():
        if palabra in texto_original:
            texto_original = texto_original.replace(palabra, reemplazo)

    blob = TextBlob(texto_original)
    try:
        blob_en = blob.translate(to='en')  # Intentamos traducir todo al inglés
    except Exception:
        blob_en = blob  # Si falla la traducción, usamos el texto original

    polaridad = blob_en.sentiment.polarity  # Obtenemos el valor de polaridad (-1 a 1)

    # Clasificamos el sentimiento según la polaridad
    if polaridad > 0.1:
        return 'positivo'
    elif polaridad < -0.1:
        return 'negativo'
    else:
        return 'neutral'

# Clase principal de la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mall Plaza Buena Vista")
        self.restaurante = None
        self.orden = []

        # Cuando se cierre la ventana, se llamará esta función
        self.root.protocol("WM_DELETE_WINDOW", self.salir_con_opiniones)

        # Frame de inicio donde se elige el restaurante
        self.frame_inicio = tk.Frame(root)
        self.frame_inicio.pack()

        tk.Label(self.frame_inicio, text="¿En qué restaurante desea comer?").pack()

        # Botones para seleccionar restaurante
        tk.Button(self.frame_inicio, text="Burger King", command=self.seleccionar_burgerking).pack()
        tk.Button(self.frame_inicio, text="McDonalds", command=self.seleccionar_mcdonalds).pack()
        tk.Button(self.frame_inicio, text="Pizza Hut", command=self.seleccionar_pizzahut).pack()
        tk.Button(self.frame_inicio, text="Salvatore Pizza", command=self.seleccionar_salvatorepizza).pack()
        tk.Button(self.frame_inicio, text="Salir", command=self.salir_con_opiniones).pack()

    # Funciones para seleccionar cada restaurante
    def seleccionar_burgerking(self):
        self.restaurante = BurgerKing()
        self.mostrar_menu()

    def seleccionar_mcdonalds(self):
        self.restaurante = McDonalds()
        self.mostrar_menu()

    def seleccionar_pizzahut(self):
        self.restaurante = PizzaHut()
        self.mostrar_menu()

    def seleccionar_salvatorepizza(self):
        self.restaurante = SalvatorePizza()
        self.mostrar_menu()

    # Muestra el menú del restaurante seleccionado
    def mostrar_menu(self):
        self.frame_inicio.pack_forget()  # Oculta el menú de inicio

        self.frame_menu = tk.Frame(self.root)
        self.frame_menu.pack()

        # Información del restaurante
        tk.Label(self.frame_menu, text=f"Bienvenido a {self.restaurante.nombre} ({self.restaurante.categoria})").pack()
        tk.Label(self.frame_menu, text=f"Horario de atención: {self.restaurante.horario}").pack()

        # Lista de platillos
        self.lista_platillos = tk.Listbox(self.frame_menu)
        for platillo, precio in self.restaurante.menu.items():
            self.lista_platillos.insert(tk.END, f"{platillo} - ${precio:.2f}")
        self.lista_platillos.pack()

        # Botones para agregar al pedido y terminar
        tk.Button(self.frame_menu, text="Agregar al pedido", command=self.agregar_pedido).pack()
        tk.Button(self.frame_menu, text="Terminar pedido", command=self.mostrar_resumen).pack()

    # Agrega un platillo al pedido
    def agregar_pedido(self):
        seleccion = self.lista_platillos.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un platillo")
            return
        indice = seleccion[0]
        platillo = list(self.restaurante.menu.items())[indice][0]
        precio = self.restaurante.menu[platillo]

        cantidad = simpledialog.askinteger("Cantidad", f"¿Cuántas unidades de {platillo} desea ordenar?", minvalue=1)
        if cantidad:
            self.orden.append((platillo, cantidad, precio))
            messagebox.showinfo("Agregado", f"Has agregado {cantidad} unidad(es) de {platillo}.")

    # Muestra el resumen del pedido
    def mostrar_resumen(self):
        if not self.orden:
            messagebox.showinfo("Pedido vacío", "No has agregado nada a tu pedido.")
        else:
            resumen = ""
            total = 0
            for nombre, cantidad, precio in self.orden:
                resumen += f"{cantidad} x {nombre} - ${precio * cantidad:.2f}\n"
                total += precio * cantidad
            resumen += f"\nTotal a pagar: ${total:.2f}"
            messagebox.showinfo("Resumen del pedido", resumen)

        self.frame_menu.pack_forget()
        self.pedir_opinion()

    # Pide opinión al usuario
    def pedir_opinion(self):
        self.frame_opinion = tk.Frame(self.root)  # Se Crea un nuevo contenedor (Frame) dentro de la ventana principal para mostrar la opinión
        self.frame_opinion.pack()  # Muestra ese contenedor en la ventana (lo hace visible)

        tk.Label(self.frame_opinion, text="¿Qué te ha parecido la comida? Escribe tu opinión:").pack()
        self.text_opinion = tk.Text(self.frame_opinion, height=5, width=40)
        self.text_opinion.pack()

        tk.Button(self.frame_opinion, text="Enviar opinión", command=self.guardar_opinion).pack()

    # Guarda la opinión del usuario y la analiza
    def guardar_opinion(self):
        opinion = self.text_opinion.get("1.0", tk.END).strip()
        if not opinion:
            messagebox.showwarning("Advertencia", "Por favor escribe una opinión.")
            return

        sentimiento = analizar_sentimiento(opinion)
        opiniones.append([self.restaurante.nombre, opinion, sentimiento])

        # Muestra mensaje dependiendo del sentimiento
        if sentimiento == 'positivo':
            messagebox.showinfo("Gracias", "¡Gracias por tu opinión positiva! 😊")
        elif sentimiento == 'negativo':
            messagebox.showinfo("Gracias", "Lamentamos que no te haya gustado. ¡Gracias por tu retroalimentación! 😔")
        else:
            messagebox.showinfo("Gracias", "Gracias por tu opinión. ¡Valoramos tus comentarios! 👍")

        # Regresamos al menú principal
        self.frame_opinion.pack_forget()  # Oculta la pantalla/opinión actual después de enviarla
        self.orden = []  # Reinicia la lista de pedidos para que esté vacía la próxima vez que se ordene
        self.restaurante = None  # Reinicia el restaurante seleccionado para que el usuario elija uno nuevo
        self.frame_inicio.pack()  # Muestra nuevamente la pantalla inicial donde se elige el restaurante

    # Se muestra las opiniones de todos los restaurantes almomento de cerrar la app
    def salir_con_opiniones(self):
        if opiniones:
            resumen = "--- Opiniones de los clientes ---\n\n"
            for idx, (rest, texto, senti) in enumerate(opiniones, 1):
                resumen += f"{idx}. Restaurante: {rest}\n"
                resumen += f"   Opinión: {texto}\n"
                resumen += f"   Sentimiento: {senti.capitalize()}\n\n"
            messagebox.showinfo("Opiniones registradas", resumen)
        else:
            messagebox.showinfo("Opiniones registradas", "No se han registrado opiniones aún.")
        self.root.destroy()  #Cerramos la app

# Inicio de la aplicación
root = tk.Tk()  # Se crea la ventana principal de la aplicación 

app = App(root)  # Crea una instancia de la clase App y le pasa la ventana 'root' para construir la interfaz

root.mainloop()  # Se Inicia el bucle principal de la aplicación , osea lo que mantiene la ventana abierta