numero=list()
continuar:bool=True

def agregar (numero:int) ->None:
    numero.append(numero)

def eliminar()->None:
    numero.pop

while continuar:
    print("Seleccione una opción")
    print("1. Agrege un numero")
    print("2. Eliminar la ultima posición")
    print("3. Salir")
    
    opción=int(input())

    if opción == 3:
        continuar=False