class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.num_paginas = nuevas_paginas
            print(f"El número de páginas se ha actualizado a: {self.num_paginas}")
        else:
            print("El número de páginas debe ser mayor que 0.")

# Crear instancias de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro2 = Libro("1984", "George Orwell", 328)

# Mostrar información de los libros
libro1.mostrar_informacion()
libro2.mostrar_informacion()

# Actualizar el número de páginas de un libro
libro1.actualizar_paginas(450)
