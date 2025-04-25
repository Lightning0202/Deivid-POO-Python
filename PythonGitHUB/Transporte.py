# Clase padre
class Transporte:
    def tipo_transporte(self):
        print("Tipo de transporte desconocido")

# Clases hijas
class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre")

class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aéreo")

class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte marítimo")

# Crear objetos
coche = Coche()
avion = Avion()
barco = Barco()

# Llamar al método tipo_transporte
coche.tipo_transporte()  # Transporte terrestre
avion.tipo_transporte()  # Transporte aéreo
barco.tipo_transporte()  # Transporte marítimo

