class Estudiante:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")

estudiante1 = Estudiante("Pepito", "Perez", 23)
estudiante2 = Estudiante("Juancho", "Smith", 19)

estudiante1.mostrar_informacion()