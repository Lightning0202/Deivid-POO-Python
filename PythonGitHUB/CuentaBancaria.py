class CuentaBancaria:
    def __init__(self, titular, codigo_titular, saldo=0):
        #Inicializa una cuenta bancaria con titular, código de titular y saldo inicial
        self.__titular = titular
        self.__codigo_titular = codigo_titular
        self.__saldo = saldo

    def depositar(self, cantidad):
       #Agrega dinero a la cuenta
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
       #Retira dinero de la cuenta si hay saldo suficiente
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self, codigo_titular):
        #Devuelve el saldo actual si el código del titular es correcto
        if codigo_titular == self.__codigo_titular:
            return self.__saldo
        else:
            return " No se puede mostrar el saldo."

    def consultar_titular(self, codigo_titular):
        #Devuelve el titular de la cuenta si el código es correcto
        if codigo_titular == self.__codigo_titular:
            return self.__titular
        else:
            return " No se puede mostrar la información del titular."


# Ejemplo de uso
cuenta = CuentaBancaria("Juan Pérez", "ABC123", 1000)  # Código de titular: ABC123

# Intentar consultar titular con un código incorrecto
print("Codigo incorrecto:", cuenta.consultar_titular("XYZ789"))

# Consultar titular y saldo con el código correcto
print("Titular de la cuenta:", cuenta.consultar_titular("ABC123"))
print("Saldo inicial:", cuenta.consultar_saldo("ABC123"))

# Operaciones bancarias
cuenta.depositar(500)
cuenta.retirar(300)

# Intento de retiro con código incorrecto (solo para demostración)
print("Codigo incorrecto:", cuenta.consultar_saldo("XYZ789"))

# Consultar saldo final con código correcto
print("Saldo final:", cuenta.consultar_saldo("ABC123"))
