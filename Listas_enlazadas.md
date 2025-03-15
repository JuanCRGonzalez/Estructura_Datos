a=Personas("Miguel")
b=Personas("Luisa")

a==b

class Node:
    def__init__(self,data):
        self.data=data
        self.next=None
______________________________________________________________________________________________________________________________________
Creación de la lista enlazada:

class ListaEnlazada
    def__init__(self):
        self.cabeza=None
______________________________________________________________________________________________________________________________________
Operaciones de las listas enlazdas
Agregar nodos

def es_vacio(self):
    return self.cabeza is None

def agregar_nodo(self,dato):
    nodo=Node(dato)
    if self.es:vacio():
        self.cabeza=nodo
    else:
        nodo_actual=self.cabeza
        while nodo_actual.next is no None:
            nodo_actual = nodo_actual.next
        nodo_actual.next=nodo

_______________________________________________________________________________________________________________________________________

Eliminar Nodo

def eliminar(self,dato):
    nodo_actual = self.cabeza
    if nodo_actual.data == dato:
        self.cabeza = nodo_actual.next
        return 
    while nodo_actual.next is not None:
        if nodo_actual.next.data == dato:
            nodo_actual.next = nodo_actual.next.next
            return
        nodo_actual = nodo_actual.next

_______________________________________________________________________________________________________________________________________


from typing import Optional

class Node:
    def__init__(self, numero:int)-> None:
        self.dato = numero
        self.next:Optional ["Node"]= None