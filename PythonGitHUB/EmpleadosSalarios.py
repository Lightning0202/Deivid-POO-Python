# Clase padre
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self._nombre = nombre           # Atributo protegido cuando se utiliza -> _ el guion bajo  y privado cuando son 2 -> __
        self._sueldo_base = sueldo_base  # Atributo protegido

    # Getter para sueldo_base
    def get_sueldo_base(self):
        return self._sueldo_base

    # Setter para sueldo_base
    def set_sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self._sueldo_base = nuevo_sueldo
        else:
            print("El sueldo no puede ser negativo.")

    def calcular_saldo(self):
        #Pero en Empleado no queremos que calcular_saldo haga nada, solo queremos definirlo para que las hijas lo implementen como ellas necesiten.
        #Sin pass, Python daría error
        pass

# Clases hijas
class EmpleadoFijo(Empleado):
    def calcular_saldo(self):
        return self.get_sueldo_base()

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_saldo(self):
        return self.get_sueldo_base() * self.horas_trabajadas

class EmpleadoTemporal(Empleado):
    def calcular_saldo(self):
        # Supongamos que a un empleado temporal se le paga el 80% de su sueldo_base
        return self.get_sueldo_base() * 0.8

#una lista de empleados
empleados = [
    EmpleadoFijo("benson", 9000),
    EmpleadoPorHoras("rigby", 2200, 160),  
    EmpleadoTemporal("Mordecai", 45500)
]

# Calcular salarios usando polimorfismo
for empleado in empleados: # Para cada empleado en la lista empleados
    print(f"Empleado: {empleado._nombre}, Salario: {empleado.calcular_saldo()}")
