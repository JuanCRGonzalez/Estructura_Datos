continuar:bool=True

def eliminar()->None:
    persona.pop

persona=dict()
def agregar_valor(clave:str, valor:str):
  persona.update({clave:valor})

while continuar:
    print("Seleccione una opción")
    print("1. Agrege un Nombre y Apellido")
    print("2. Eliminar la ultima posición")
    print("3. Salir")
    opción=int(input())

    if opción == 1:
        str(input(agregar_valor))
        print(agregar_valor)
    elif opción ==2:
        continuar= eliminar
    elif opción == 3:
        continuar=False

            

