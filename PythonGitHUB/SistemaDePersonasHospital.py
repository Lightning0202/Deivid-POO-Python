class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.edad = edad  # usa setter para validar
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if valor >= 0:
            self.__edad = valor
        else:
            raise ValueError("La edad no puede ser negativa.")

    @property
    def documento(self):
        return self.__documento



class Paciente(Persona):
    def __init__(self, nombre, edad, documento, diagnostico):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = diagnostico
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico

    def _actualizar_diagnostico(self, nuevo_diagnostico):  # solo lo usa el doctor
        self.__diagnostico = nuevo_diagnostico





class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._actualizar_diagnostico(nuevo_diagnostico)
            print("Diagnóstico actualizado correctamente.")
        else:
            print("Solo se puede modificar el diagnóstico de un paciente.")





paciente1 = Paciente("Pepito fonseca", 30, "15234678", "Gripe")
doctor1 = Doctor("Dra. Peres", 35, "029392321", "Medicina General")

paciente1.agregar_historial("Consulta 2024 - Síntomas leves")
paciente1.agregar_historial("Consulta 2025 - Mejora significativa")

print("Historial del paciente:", paciente1.ver_historial())
print("Diagnóstico inicial:", paciente1.ver_diagnostico())

doctor1.modificar_diagnostico(paciente1, "Recuperado completamente")
print("Nuevo diagnóstico:", paciente1.ver_diagnostico())



