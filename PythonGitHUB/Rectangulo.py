class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            print("Error: El largo y el ancho deben ser mayores que cero")
        else:
            self.largo = largo
            self.ancho = ancho

    def cambiar_dimensiones(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.largo = largo
            self.ancho = ancho
        else:
            print("Error: Las dimensiones deben ser mayores que cero")

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)

    def mostrar_dimensiones(self):
        print(f"Largo: {self.largo}, Ancho: {self.ancho}")



r = Rectangulo(4, 2)
r.mostrar_dimensiones()
print("Área:", r.area())
print("Perímetro:", r.perimetro())

r.cambiar_dimensiones(5, 3)
r.mostrar_dimensiones()
