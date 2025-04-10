class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def mostrar_info(self):
        print(f'Nombre: {self.nombre}, Especie: {self.especie}')


class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie) 
        self.raza = raza

    def mostrar_raza(self):
        print(f'Raza: {self.raza}')


# se crea al perro
perro1 = Perro("Max", "Canino", "Labrador")


perro1.mostrar_info()     # Método heredado de Animal
perro1.mostrar_raza()     # Método propio de Perro
