class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
        else:
            self.velocidad_actual = self.velocidad_maxima
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
        else:
            self.velocidad_actual = 0
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self, velocidad_limite):
        if self.velocidad_actual > velocidad_limite:
            print("¡Atención! El vehículo supera el límite de velocidad.")
        else:
            print("La velocidad está dentro del límite permitido.")


vehiculo = Vehiculo("Tesla", "Model S", 250)


while True:
    print("\n--- Menú ---")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        incremento = int(input("¿Cuánto deseas acelerar (km/h)? "))
        vehiculo.acelerar(incremento)
    elif opcion == "2":
        decremento = int(input("¿Cuánto deseas frenar (km/h)? "))
        vehiculo.frenar(decremento)
    elif opcion == "3":
        limite = int(input("Introduce el límite de velocidad a verificar (km/h): "))
        vehiculo.verificar_limite(limite)
    elif opcion == "4":
        print("Saliendo del programa")
        break
    else:
        print("Opcion invalidad Intenta de nuevo")
