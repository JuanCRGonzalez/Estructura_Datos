# Esta clase representa un nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor          # El valor del nodo
        self.izquierdo = None       # Enlace al hijo izquierdo
        self.derecho = None         # Enlace al hijo derecho

# Esta clase representa el árbol binario completo
class Arbol:
    def __init__(self):
        self.raiz = None            # La raíz del árbol empieza vacía

    # Esta función sirve para insertar un nuevo valor al árbol de forma recursiva
    def insertar(self, nodo, valor):
        if nodo is None:
            # Si el lugar está vacío, se crea un nuevo nodo con el valor
            return Nodo(valor)
        if valor < nodo.valor:
            # Si el valor es menor, va a la izquierda
            nodo.izquierdo = self.insertar(nodo.izquierdo, valor)
        else:
            # Si el valor es mayor o igual, va a la derecha
            nodo.derecho = self.insertar(nodo.derecho, valor)
        return nodo

    # Esta función se llama desde afuera para insertar fácilmente
    def agregar(self, valor):
        self.raiz = self.insertar(self.raiz, valor)

    # Esta función recorre el árbol en preorden (nodo -> izquierdo -> derecho)
    def mostrar_preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor)                          # Mostrar valor del nodo actual
            self.mostrar_preorden(nodo.izquierdo)      # Visitar hijo izquierdo
            self.mostrar_preorden(nodo.derecho)        # Visitar hijo derecho

# Crear el árbol y agregar los valores uno por uno
mi_arbol = Arbol()
valores = [20, 10, 30, 5, 15, 25, 35]  # Valores a insertar

for numero in valores:
    mi_arbol.agregar(numero)

# Mostrar el árbol en preorden
print("Mostrando árbol en preorden:")
mi_arbol.mostrar_preorden(mi_arbol.raiz)