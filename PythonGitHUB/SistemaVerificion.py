class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar(clave_acceso)  # Guardar la clave cifrada

    # Método para cifrar (reversar la cadena)
    def __cifrar(self, clave):
        return clave[::-1] # es una forma basica de cifrado que simplemente invierte el orden de los caracteres de la cadena es decir (clave se vuelve-> evalc). 

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    def verificar_clave(self, clave_ingresada):
        return self.__cifrar(clave_ingresada) == self.__clave_acceso

    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):  #se verifica si la clave antigua es correcta 
            self.__clave_acceso = self.__cifrar(nueva_clave)
            print("Clave actualizada correctamente.")
        else:
            print("La clave antigua no es correcta.")

# Ejemplo de uso:
empleado1 = Empleado("Ana", "Administrador", "clave123")

print(f'Nombre: {empleado1.nombre}')
print(f'Rol: {empleado1.rol}')

# Verificando la clave
print("Clave correcta:", empleado1.verificar_clave("clave123"))     #good 
print("Clave incorrecta:", empleado1.verificar_clave("otra_clave"))  #error

# Cambiando clave
empleado1.cambiar_clave("clave123", "nueva123")
print("Nueva clave verificada:", empleado1.verificar_clave("nueva123"))  #good

# Verificando  que no pase con clave antigua errada
empleado1.cambiar_clave("clave122", "nueva123")
