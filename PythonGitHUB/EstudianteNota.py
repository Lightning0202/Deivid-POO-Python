class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def estado(self):
        if self.calificacion >= 60:
            return "Aprobado"
        else:
            return "Reprobado"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificación: {self.calificacion}")
        print(f"Estado: {self.estado()}")



alumno1 = Estudiante("Laura", 17, 75)
alumno1.mostrar_info()
