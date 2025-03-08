Vehiculo->Clase
----------------------------------------------------------------------------------------------------------------------------------------
Color                    |                             Moto (Color,Modelo, Cilindraje)
Modelo                   |<-ATRIBUTOS                  Carro (Color,Modelo, Cilindraje)
cilindraje               |                             Bus (Color,Modelo, Cilindraje)
numero-ruedas            |

Encender                 |
Acelerar                 |<-METODOS
Frenar                   |
Apagar                   |
________________________________________________________________________________________________________________________________________
class vehiculo:
    color:str
    modelo:int
    cilindraje:int
    numero_ruedas:int

def encender(self):
    pass
________________________________________________________________________________________________________________________________________
Consultar: Metodos Magicos
