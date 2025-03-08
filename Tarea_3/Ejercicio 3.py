class Empleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajador_en_funcion(self):
        return f"{self.nombre} está trabajando."

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def supervisar_equipo(self):
        return f"{self.nombre} está supervisando al equipo."

    def trabajador_en_funcion(self):
        return f"{self.nombre} está supervisando al equipo."

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguaje_de_programacion: str):
        super().__init__(nombre, salario, departamento)
        self.lenguaje_de_programacion = lenguaje_de_programacion

    def programador_en_funcion(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje_de_programacion}."

    def trabajador_en_funcion(self):
        return f"{self.nombre} está desarrollando software en {self.lenguaje_de_programacion}."
    

#------------------------------------------------------------------------------------------------------------------------------


class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumo_energia: float):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energia = consumo_energia

    def encender(self):
        return f"El electrodoméstico {self.marca} {self.modelo} está encendido."

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo_energia: float, capacidad: float):
        super().__init__(marca, modelo, consumo_energia)
        self.capacidad = capacidad

    def iniciar_ciclo_de_lavado(self):
        return f"La lavadora {self.marca} está iniciando el ciclo de lavado."

    def encender(self):
        return f"La lavadora {self.marca} está encendida y lista para lavar."

class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo_energia: float, tiene_congelador: bool):
        super().__init__(marca, modelo, consumo_energia)
        self.tiene_congelador = tiene_congelador

    def regulador_temperatura(self):
        return f"El refrigerador {self.marca} está regulando la temperatura."

    def encender(self):
        return f"El refrigerador {self.marca} está encendido y regulando la temperatura."
    

#--------------------------------------------------------------------------------------------------------------------------------


class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def iniciar_sesion(self, nombre_de_usuario: str, contraseña: str):
        if self.nombre_usuario == nombre_de_usuario and self.contraseña == contraseña:
            return f"Bienvenido, {self.nombre_usuario}."
        else:
            return "Credenciales incorrectas."

class Administrador(Usuario):
    def gestionar_usuarios(self):
        return f"El administrador {self.nombre_usuario} está gestionando los usuarios."

    def iniciar_sesion(self, nombre_usuario: str, contraseña: str):
        # Los administradores pueden tener credenciales especiales.
        return super().iniciar_sesion(nombre_usuario, contraseña)

class Cliente(Usuario):
    def realizar_compra(self):
        return f"El cliente {self.nombre_usuario} está realizando una compra."

    def iniciar_sesion(self, nombre_usuario: str, contraseña: str):
        # Los clientes tienen acceso básico con sus credenciales.
        return super().iniciar_sesion(nombre_usuario, contraseña)