# Clase para representar una pila
class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def meter(self, valor):
        self.elementos.append(valor)

    def sacar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        else:
            return None

    def ver_ultimo(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        else:
            return None

# Función para verificar si los símbolos están balanceados
def revisar_balanceo(texto):
    pila = Pila()
    abiertos = "({["
    cerrados = ")}]"
    pares = {"(": ")", "{": "}", "[": "]"}

    for i in range(len(texto)):
        letra = texto[i]

        if letra in abiertos:
            pila.meter((letra, i))  # Guarda el símbolo y su posición
        elif letra in cerrados:
            tope = pila.ver_ultimo()

            if tope is None:
                return False, i  # No hay abierto para este cerrado

            if pares[tope[0]] != letra:
                return False, i  # No coincide el par

            pila.sacar()

    if pila.esta_vacia():
        return True, -1
    else:
        simbolo_restante = pila.ver_ultimo()
        return False, simbolo_restante[1]

# Ejemplo de uso
texto = "{[a + b] * (c - d)}"
resultado, lugar = revisar_balanceo(texto)

if resultado:
    print("La expresión está balanceada.")
else:
    print("La expresión NO está balanceada. Error en la posición", lugar)