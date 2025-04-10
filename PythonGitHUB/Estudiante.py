class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  
        self.grado = grado

    def mostrar_grado(self):
        print(f'Grado: {self.grado}')


# Se crea la instancia del estudiante
estudiante1 = Estudiante("María", 16, "10° grado")


estudiante1.mostrar_datos()    # Heredado de Persona
estudiante1.mostrar_grado()    # Método propio de Estudiante
