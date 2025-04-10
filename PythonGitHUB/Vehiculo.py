class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def mostrar_info(self):
        print(f'Marca: {self.marca}, Año: {self.año}')


class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)  
        self.modelo = modelo

    def mostrar_modelo(self):
        print(f'Modelo: {self.modelo}')


# Se crea una instancia de un coche 
mi_coche = Coche("Toyota", 2022, "Corolla")


mi_coche.mostrar_info()     # Método heredado de Vehiculo
mi_coche.mostrar_modelo()   # Método propio de Coche
