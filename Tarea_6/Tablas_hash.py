class Persona:
    nombre =""
    telefono =""
    direccion =""

p = Persona
p.nombre = "Miguel"
p.telefono = "333445"
p.direccion = "Calle D Manzana 13"

trablash= list()

print(hash(p.nombre), hash(p.telefono), hash(p.direccion))