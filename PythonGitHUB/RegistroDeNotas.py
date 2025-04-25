class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado, codigo):
        super().__init__(nombre, edad)
        self.__codigo = None
        self.__notas = []
        self.grado = grado
        self.codigo = codigo  # se usa el setter con validación

    @property #osea al llamarlo property se convierte en getter
    def nombre(self):
        return self._nombre

    @nombre.setter # para convertirlo en setter debo poner @nombre.setter
    def nombre(self, valor):
        if valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre no puede estar vacío.")

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if valor.isalnum():
            self.__codigo = valor
        else:
            raise ValueError("El código debe ser alfanumérico.")

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

    def calcular_promedio(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

    def mostrar_grado(self):
        print(f'Grado: {self.grado}')

    def mostrar_promedio(self):
        print(f'Promedio: {self.calcular_promedio():.2f}')

    def mostrar_estado(self):
        estado = "Aprobado" if self.es_aprobado() else "No aprobado"
        print(f'Estado: {estado}')


# Ejemplo de uso
estudiante1 = Estudiante("María", 16, "10° grado", "B456")
estudiante1.agregar_nota(4.0)
estudiante1.agregar_nota(3.2)
estudiante1.agregar_nota(2.9)

estudiante1.mostrar_datos()      # Heredado de Persona
estudiante1.mostrar_grado()      # Método propio de Estudiante
estudiante1.mostrar_promedio()   # Muestra el promedio
estudiante1.mostrar_estado()     # Muestra si está aprobado
