from enum import Enum
from abc import ABC, abstractmethod

#Enums
class Rol(Enum):
    BARISTA = "BARISTA"
    MESERO = "MESERO"
    GERENTE = "GERENTE"

class Temperatura(Enum):
    FRIA = "FRIA"
    CALIENTE = "CALIENTE"

class Estado(Enum):
    PENDIENTE = "PENDIENTE"
    PREPARADO = "PREPARADO"
    ENTREGADO = "ENTREGADO"

#Personas
class Persona(ABC):
    def __init__(self, idPersona: int, nombre: str, email:str):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(f"Sesión iniciada correctamente. Bienvenid@ {self.nombre}")

    def actualizarPerfil(self):
        print(f"Perfil de {self.nombre} actualizado correctamente")

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad: int = 0
        self.historialPedidos: list = []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        print(f"Pedido {pedido.idPedido} resgistrado correctamente para {self.nombre}")

    def consultarHistorial(self):
        return self.historialPedidos

    def canjearPuntos(self):
        print(f"Canjeando puntos de {self.nombre}. . ")

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email, idEmpleado: str, rol: Rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado = idEmpleado
        self.rol = rol

    def actualizarInventario(self):
        print(f"Empleado {self.nombre} actualizadó inventario correctamente")

    def cambiarEstadoPedido(self, pedido, nuevoEstado: Estado):
        pedido.estado = nuevoEstado
        print(f"Estado del pedido {pedido.idPedido} cambiado a {nuevoEstado.value}")

#Productos
class ProductoBase:
    def __init__(self, idProducto: int, nombre: str, precioBase: float):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precioBase = precioBase

class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, tamano: str, temperatura: Temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamano = tamano
        self.temperatura = temperatura
        self.modificadores: list = []

    def agregarExtra(self, extra: str):
        self.modificadores.append(extra)
        print(f"Se agregó el extra {extra} a la bebida {self.nombre}")

    def calcularPrecioFinal(self):
        return self.precioBase + (len(self.modificadores) * 5.0)
    
class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase, esVegano: bool, sinGluten: bool):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

#Ventas
class Pedido:
    def __init__(self, idPedido: int):
        self.idPedido = idPedido
        self.productos: list = []
        self.estado: Estado = Estado.PENDIENTE
        self.total: float = 0.0

    def calcularTotal(self):
        total = 0.0
        for p in self.productos:
            if isinstance(p, Bebida):
                total += p.calcularPrecioFinal()
            else:
                total += p.precioBase
        self.total = total
        return self.total
    
    def validarStock(self, inventario):
        return len(inventario.ingredientes) > 0
    
class Inventario:
    def __init__(self):
        self.ingredientes: dict = {"café": 50, "Leche": 40}

    def reducirStock(self, ingrediente:str, cantidad: int):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente] -= cantidad

    def notificarFaltante(self):
        for ingrediente, cantidad in self.ingredientes.items():
            if cantidad <= 5:
                print(f"Faltan {cantidad} unidades de {ingrediente}")
