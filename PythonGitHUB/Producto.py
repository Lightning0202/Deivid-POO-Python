class Producto:
    def __init__(self, nombre, precio):
        #Inicializa un producto con nombre y precio, asegurando que el precio sea válido.
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__nombre = nombre
        self.__precio = precio

    def cambiar_precio(self, nuevo_precio):
        #Cambia el precio del producto si es mayor que cero
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"Precio actualizado: {self.__precio}")
        else:
            raise ValueError("El nuevo precio debe ser mayor que cero.")

    def consultar_precio(self):
        #Devuelve el precio actual del producto
        return self.__precio

    def obtener_nombre(self):
        #Devuelve el nombre del producto
        return self.__nombre

    def aplicar_descuento(self, porcentaje):
        #Aplica un descuento al precio si el porcentaje está entre 0 y 100
        if 0 <= porcentaje <= 100:
            descuento = (self.__precio * porcentaje) / 100
            self.__precio -= descuento
            print(f"Descuento aplicado del {porcentaje}%. Nuevo precio: {self.__precio}")
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")


# Ejemplo de uso ingresando un producto
producto = Producto("Smartphone", 500)

# Consultamos la  información del producto
print("Nombre del producto:", producto.obtener_nombre())
print("Precio actual:", producto.consultar_precio())

# Se cambia  el precio
producto.cambiar_precio(450)

# Se aplica el descuento válido
producto.aplicar_descuento(10)

# Se aplica un descuento inválido Para Comprobar las validaciones
try:
    producto.aplicar_descuento(120)
except ValueError as e:
    print("Error:", e)

# se intenta cambiar el precio a un valor no válido (debe lanzar error)
try:
    producto.cambiar_precio(-50)
except ValueError as e:
    print("Error:", e)
