class Vehiculo:
    marca: str
    modelo: int
    color: str
    cilindraje: int
    numero_ruedas: int
    combustible: int
    tipo: str

    def __init__(self, marca: str, combustible: int, tipo: str) -> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def __str__(self) -> str:
        return f"La marca del vehiculo es {self.marca}, el nivel de combustible es de {self.combustible} y es tipo {self.tipo}"

    def encender(self):
        if self.combustible < 10:
            return "Necesita llenar de gasolina"
        else:
            return "El combustible es suficiente"

    def marchar(self):
        if self.combustible > 0:
            self.combustible -= 1
            if self.combustible < 10:
                return f"El nivel de combustible está bajo ({self.combustible})"
            else:
                return f"El vehículo está en marcha, nivel de combustible: {self.combustible}"
        else:
            return "El combustible ha llegado a 0, el vehículo se detiene."

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def apagar(self):
        pass

class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
    pass


vehiculo1 = Vehiculo("Mazda", 8, "carro")
print(vehiculo1)
print(vehiculo1.encender())

for _ in range(10):
    print(vehiculo1.marchar())

moto1 = Moto("Honda", 50, "moto")
print(moto1)

carro1 = Carro("Renault", 70, "carro")
print(carro1)