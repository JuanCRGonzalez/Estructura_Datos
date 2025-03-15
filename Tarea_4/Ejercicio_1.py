class Animal:
    def __init__(self, nombre_animal, edad_animal, tipo_animal):
        self.nombre_animal = nombre_animal
        self.edad_animal = edad_animal
        self.tipo_animal = tipo_animal
    
    def get_nombre_animal(self):
        return self.nombre_animal
    
    def get_edad_animal(self):
        return self.edad_animal
    
    def get_tipo_animal(self):
        return self.tipo_animal
    
    def set_nombre(self, nombre_animal):
        self.nombre_animal = nombre_animal
    
    def set_edad(self, edad_animal):
        self.edad_animal = edad_animal
    
    def set_tipo(self, tipo_animal):
        self.tipo_animal = tipo_animal
    
    def mostrar_datos_animal(self):
        return f"Nombre: {self.nombre_animal}, Edad: {self.edad_animal}, Tipo: {self.tipo_animal}"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        if not self.existe_animal(animal):
            nuevo_nodo = Nodo(animal)
            if self.cabeza is None:
                self.cabeza = nuevo_nodo
            else:
                nodo_actual = self.cabeza
                while nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
        else:
            print(f"El animal {animal.get_nombre_animal()} ya está registrado.")

    def existe_animal(self, animal):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.animal.get_nombre_animal() == animal.get_nombre_animal() and nodo_actual.animal.get_tipo_animal() == animal.get_tipo_animal():
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def mostrar_animales_iterativo(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.animal.mostrar_datos_animal())
            nodo_actual = nodo_actual.siguiente

    def mostrar_animales_metodo_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo:
            print(nodo.animal.mostrar_datos_animal())
            self.mostrar_animales_metodo_recursivo(nodo.siguiente)

animal1 = Animal("Leon", 5, "Felino")
zoologico = ListaEnlazada()
zoologico.agregar_animal(animal1)
print("Mostrar animales de manera en recurso iterativo:")
zoologico.mostrar_animales_iterativo()

