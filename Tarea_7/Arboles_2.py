# Esta función busca un valor en el árbol binario
def buscar(nodo, valor_buscado):
    if nodo is None:
        # Si llegamos a un espacio vacío, no está
        return False
    if nodo.valor == valor_buscado:
        # Si el valor del nodo es el que buscamos
        return True
    elif valor_buscado < nodo.valor:
        # Si el valor buscado es menor, buscar en la izquierda
        return buscar(nodo.izquierdo, valor_buscado)
    else:
        # Si el valor buscado es mayor, buscar en la derecha
        return buscar(nodo.derecho, valor_buscado)

# Probar la búsqueda con algunos valores
print("Buscando valores en el árbol:")
print("¿Está el 15?", buscar(mi_arbol.raiz, 15))  # True
print("¿Está el 40?", buscar(mi_arbol.raiz, 40))  # False