class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Calificación: {self.calificacion}")

    def verificar_aprobacion(self):
        if self.calificacion >= 60:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} ha reprobado.")

# Crear instancias de la clase Estudiante
estudiante1 = Estudiante("felipe mendez", 20, 75)
estudiante2 = Estudiante("Ana de armas", 19, 58)

# Mostrar información de los estudiantes
estudiante1.mostrar_informacion()
estudiante1.verificar_aprobacion()

print("\n")

estudiante2.mostrar_informacion()
estudiante2.verificar_aprobacion()
