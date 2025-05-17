# Clase para guardar la información de una persona
class Persona:
    def __init__(self, codigo, nombre, numero):
        self.codigo = codigo
        self.nombre = nombre
        self.numero = numero

    # Esta función sirve para mostrar los datos de la persona
    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.numero}"

# Clase que guarda varias personas (como una agenda de teléfonos)
class Libreta:
    def __init__(self, espacios=10):
        self.espacios = [[] for _ in range(espacios)]
        self.limite = espacios

    # Esta función saca un número para saber en qué lugar guardar o buscar
    def calcular_posicion(self, codigo):
        return hash(str(codigo)) % self.limite

    # Guardar una persona nueva
    def guardar(self, persona):
        lugar = self.calcular_posicion(persona.codigo)

        # Revisar si ya está guardado
        for p in self.espacios[lugar]:
            if p.codigo == persona.codigo:
                print(f"Ya hay una persona con el código {persona.codigo}")
                return False

        self.espacios[lugar].append(persona)
        print(f"{persona.nombre} guardado en el lugar {lugar}")
        return True

    # Otra forma de guardar usando nombre y número directamente
    def guardar_datos(self, nombre, numero):
        if len(self.espacios) < 10:
            clave = hash(nombre)
            lugar = self.calcular_posicion(clave)
            self.espacios[lugar].append((nombre, numero, clave))
            print("\nSe guardó un nuevo contacto:")
            print(f"  Nombre: {nombre}")
            print(f"  Tel: {numero}")
            print(f"  Código interno: {clave}")
            print(f"  Lugar en lista: {lugar}")
        else:
            print("La libreta ya no tiene más espacio.")

    # Buscar a alguien por su código
    def buscar_persona(self, codigo):
        lugar = self.calcular_posicion(codigo)
        for p in self.espacios[lugar]:
            if isinstance(p, Persona) and p.codigo == codigo:
                return p
        return None

    # Quitar a una persona de la lista
    def quitar(self, codigo):
        lugar = self.calcular_posicion(codigo)
        for i, p in enumerate(self.espacios[lugar]):
            if isinstance(p, Persona) and p.codigo == codigo:
                del self.espacios[lugar][i]
                print(f"Se eliminó a la persona con código {codigo}")
                return True
        print(f"No se encontró a nadie con ese código: {codigo}")
        return False

    # Mostrar todo lo que hay en la libreta
    def ver_todo(self):
        print("\nLIBRETA DE CONTACTOS")
        for i, grupo in enumerate(self.espacios):
            if grupo:
                print(f"Espacio {i}:")
                for p in grupo:
                    print(f"  {p}")

# Parte principal del programa
if __name__ == "__main__":
    libreta = Libreta(5)

    # Agregamos personas
    libreta.guardar(Persona("101", "Juan Pérez", "111-2222"))
    libreta.guardar(Persona("102", "Lucía Torres", "333-4444"))
    libreta.guardar(Persona("103", "Mario Díaz", "555-6666"))

    # Agregar usando la otra función
    libreta.guardar_datos("Elena Ruiz", "777-8888")
    libreta.guardar_datos("Tomás Vargas", "999-0000")

    # Buscar una persona
    print("\nBuscando a la persona con código 102:")
    resultado = libreta.buscar_persona("102")
    if resultado:
        print("Encontrado:", resultado)
    else:
        print("No está en la libreta.")

    # Ver toda la libreta
    libreta.ver_todo()

    # Quitar un contacto
    libreta.quitar("102")

    # Ver la libreta otra vez
    libreta.ver_todo()