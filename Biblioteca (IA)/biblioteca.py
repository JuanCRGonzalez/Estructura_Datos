class Libro:
    def __init__(self,titulo, autor, editorial, fecha_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.disponible = True

def mostrar_info(self):
    return f"{self.titulo} por {self.autor}, ISBN;{self.isbn}"


def actualizar_disponibilidad(self, disponible):
    self.disponible = disponible
    estado = "disponible" if disponible else "no disponible"
    print(f"El libro {self.titulo} ahora está {estado}")

class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.libros_prestados =[]

def prestar_libro(self, libro, usuario):
    if libro.disponible:
        self.libros_prestados.append(libro)
        libro.actualizar_disponibilidad(False)
        print(f"Libro {libro.titulo} prestado a {self.nombre}.")
    else:
        print("Este libro no se encuentra disponible")

def devolver_libro(self, libro):
    if libro in self.libro_prestado:
        self.libros_prestados.quitar(libro)
        libro.actualizar_disponibilidad(True)
        print(f"Libro{libro.titulo} devuelto por {self.nombre}")

class Bibliotecario:
    def __init__(self, id_bibliotecario, nombre):
        self.id_bibliotecario = id_bibliotecario
        self.nombre = nombre

    def añadir_libro(self, biblioteca, libro):
        biblioteca.libros.append(libro)
        print(f"Libro {libro.titulo} añadido al sistema")

    def eliminar_libro (self, biblioteca, libro):
        if libro in biblioteca.libro:
            biblioteca.libro.quitar(libro)
            print (f"Libro {libro.titulo} fue eliminado del sistema")
        else:
            print("Este libro no está registrado en el sistema")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self. usuarios = []
        self.bibliotecarios = []
        self. prestamo = []

    def registrar_usuarios(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} está registrado en el sistema")

    def eliminar_usuario(self, usuario):
        if usuario in self.usuario:
            self.usuarios.quitar(usuario)
            print(f"Usuario{usuario.nombre} fue eliminado del sistema")

    def listar_libros(self):
        for libro in self.libro:
            print(libro.mostrar_info())

    def listar_usuario(self):
        for usuario in self.usuario:
            print(f"{usuario.nombre}, Email: {usuario.email}")

class Prestamo:
    def __init__(self, id_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

def finalizar_prestamo(self):
    print(f"Prestamo del libro {self.libro.titulo} finalizado, debe ser devuelto por {self.usuario.nombre} antes de {self.fecha_devolucion}")
