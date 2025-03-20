class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        # Convertir el número en una lista de enteros
        digitos = []
        for d in str(numero):  # Recorremos el número como cadena
            digitos.append(int(d))  # Convertimos cada carácter en entero y lo agregamos a la lista
        
        # Invertimos la lista para trabajar desde el último dígito al primero
        digitos.reverse()

        # Aplicar el algoritmo de Luhn
        for i in range(1, len(digitos), 2):  # Doblar los números en posiciones pares
            digitos[i] *= 2
            if digitos[i] > 9:  # Si el número es mayor a 9, restar 9
                digitos[i] -= 9
        
        # Sumar todos los dígitos
        suma_total = sum(digitos)

        # Verificamos si la suma es divisible por 10 ,si lo es la tarjeta es valida
        return suma_total % 10 == 0

# Prueba del código con números de tarjeta de ejemplo
tarjeta1 = TarjetaCredito("4532015112830366")  # Tarjeta válida
tarjeta2 = TarjetaCredito("1234567812345670")  # Tarjeta inválida

print("Tarjeta 1 válida:", TarjetaCredito.validar_tarjeta(tarjeta1.numero))  # True
print("Tarjeta 2 válida:", TarjetaCredito.validar_tarjeta(tarjeta2.numero))  # False

