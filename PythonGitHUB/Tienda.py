class Producto:
    def __init__(self, nombre, precio, stock):
        """Inicializa un producto con su nombre, precio y cantidad en stock."""
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock_suficiente(self, cantidad):
        #Verifica si hay suficiente stock para vender la cantidad solicitada
        return self.stock >= cantidad

    def realizar_venta(self, cantidad):
        #Intenta vender la cantidad especificada del producto
        #Si hay stock suficiente, se descuenta; de lo contrario, se informa la falta de disponibilidad
        if self.hay_stock_suficiente(cantidad):
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f"Stock insuficiente para vender {cantidad} unidades de {self.nombre}. Stock disponible: {self.stock}.")

    def agregar_stock(self, cantidad):
        #Aumenta el stock del producto en la cantidad especificada
        self.stock += cantidad
        print(f" Se añadieron {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}.")

# Creación de un producto con valores iniciales
producto = Producto("Laptop", 1200, 10)

# Verificar disponibilidad y realizar ventas según el enunciado
print("\n ¿Hay al menos 5 unidades disponibles?", producto.hay_stock_suficiente(5))
producto.realizar_venta(3)

print("\n ¿Hay al menos 8 unidades disponibles?", producto.hay_stock_suficiente(8))
producto.realizar_venta(8)  # Esta venta no debe completarse por falta de stock

print("\n Añadiendo 10 unidades más al stock.")
producto.agregar_stock(10)

print("\n ¿Hay al menos 8 unidades disponibles ahora?", producto.hay_stock_suficiente(8))
producto.realizar_venta(8)  # Ahora la venta debe realizarse con éxito

