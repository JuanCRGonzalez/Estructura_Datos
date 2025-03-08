class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def tener_nombre(self) -> str:
        return self.nombre

    def dar_nombre(self, nombre: str):
        self.nombre = nombre

    def tener_edad(self) -> int:
        return self.edad

    def dar_edad(self, edad: int):
        self.edad = edad

    def tener_genero(self) -> str:
        return self.genero

    def dar_genero(self, genero: str):
        self.genero = genero

    def dar_información(self):
        return f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}."
    
#-------------------------------------------------------------------------------------------------------------------------------

class CuentaBancaria:
    def __init__(self, propietario: Persona, dinero: float, numero_de_cuenta: str):
        self.propietario = propietario
        self.dinero = dinero
        self.numero_de_cuenta = numero_de_cuenta

    def depositar(self, cantidad: float):
        if cantidad > 0:
            self.dinero += cantidad
            return f"Dinero depositado. Nueva cantidad de dinero: {self.dinero}."
        else:
            return "Cantidad de depósitada no válida."

    def retirar(self, cantidad: float):
        if cantidad > 0 and cantidad <= self.dinero:
            self.saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.dinero}."
        elif cantidad > self.dinero:
            return "Cantidad de dinero insuficiente insuficiente."
        else:
            return "Cantidad de retiro no válida."

    def consultar_saldo(self):
        return f"Saldo actual: {self.dinero}."
    

#-------------------------------------------------------------------------------------------------------------------------------

#class Rectangulo:
#No pude hacerlo

#--------------------------------------------------------------------------------------------------------------------------------

class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, año_de_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_de_publicacion = año_de_publicacion

    def dar_titulo(self) -> str:
        return self.titulo

    def escribir_titulo(self, titulo: str):
        self.titulo = titulo

    def dar_autor(self) -> str:
        return self.autor

    def escribir_autor(self, autor: str):
        self.autor = autor

    def mostrar_informacion_libro(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nGénero: {self.genero}\nAño de Publicación: {self.año_de_publicacion}"
    

#-------------------------------------------------------------------------------------------------------------------------------


class Cancion:
    def __init__(self, titulo: str, artista: str, album: str, duracion: str):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def dar_titulo(self) -> str:
        return self.titulo

    def escribir_titulo(self, titulo: str):
        self.titulo = titulo

    def reproducir_musica(self):
        return f"Se está reproduciendo la canción {self.titulo} de {self.artista} del álbum {self.album}."
    

#------------------------------------------------------------------------------------------------------------------------------


class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def dar_nombre(self) -> str:
        return self.nombre

    def escribir_nombre(self, nombre: str):
        self.nombre = nombre

    def total(self, cantidad: int) -> float:
        if cantidad <= self.cantidad_disponible:
            return cantidad * self.precio
        else:
            return "Cantidad insuficiente disponible."
        