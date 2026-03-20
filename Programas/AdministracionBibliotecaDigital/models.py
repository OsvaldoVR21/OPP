from datetime import date, timedelta
from typing import List, Optional

class Material:
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.añoPublicacion = añoPublicacion
        self.disponible = True
    
class Libro(Material):
    def __init__(self, idMaterial:int, titulo: str, añoPublicacion: int, autor: str, isbn: str, genero: str):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero

class Revista(Material):
    def __init__(self, idMaterial: int, titlo: str, añoPublicacion: int, edicion: int, periodicidad: str):
        super().__init__(idMaterial, titlo, añoPublicacion)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, idMaterial: int, titulo: str, añoPublicacion: int, tipoArchivo: str, urlDescarga: str, tamañoMB: float):
        super().__init__(idMaterial, titulo, añoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamañoMB = tamañoMB

#usuarios y sedes
class Persona: 
    def __init__(self, idPersona: int, nombre: str):
        self.idPersona = idPersona
        self.nombre = nombre

class Usuario(Persona):
    def __init__(self, idPersona: int, nombre: str, limitePrestamos: int=3):
        super().__init__(idPersona, nombre)
        self.limitePrestamos = limitePrestamos
        self.listaActiva: List['Prestamo'] = []
        self.bloqueado = False

class Bibliotecario(Persona):
    def __init__(self, idPersona: int, nombre: str):
        super().__init__(idPersona, nombre)

    def gestionarPrestamo(self, usuario: Usuario, material:Material):
        if len(usuario.listaActiva) < usuario.limitePrestamos and material.disponible:
            nuevo_prestamo = Prestamo(100, date.today(), None, usuario,material)
            usuario.listaActiva.append(nuevo_prestamo)
            material.disponible = False
            print(f"Préstamo exitoso: {material.titulo}")
            return nuevo_prestamo
        print("No se pudo realizar el préstamo")
        return None
    
    def transferirMaterial(self, material: Material, sucursalDestino: 'Sucursal'):
        sucursalDestino.catalogoLocal.append(material)
        print(f"Material {material.titulo} transferido a {sucursalDestino.nombre}")

class Sucursal:
    def __init__(self, idSucursal: int, nombre: str):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal: List[Material] = []

#gestion prestamos
class Prestamo:
    def __init__(self, idPrestamo: int, fechaInicio: date, fechaDevolucion: Optional[date], usaurio: Usuario, material: Material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usaurio = usaurio
        self.material = material

class Penalizacion:
    def __init__(self, monto: float, motivo: str, pagada: bool=False):
        self.monto = monto
        self.motivo = motivo
        self.pagada = pagada

    def clacularMulta(self, dias_retraso: int):
        self.monto = dias_retraso * 1.5
        return self.monto

    def bloquearUsuario(self, usuario: Usuario):
        if not self.pagada:
            usuario.bloqueado = True
            print(f"Usuario {usuario.nombre} bloqueado")

class Catalogo:
    def __init__(self, todas_las_sucursales: List[Sucursal]):
        self.sucursales = todas_las_sucursales

    def buscarPorAutor(self, autor: str):
        resultados=[]
        for suc in self.sucursales:
            for mat in suc.catalogoLocal:
                if isinstance(mat, Libro) and mat.autor.lower() == autor.lower():
                    resultados.append(mat)
        return resultados

    def buscarEnTodasSucursales(self, titulo: str):
        for suc in self.sucursales:
            for mat in suc.catalogoLocal:
                if titulo.lower() in mat.titulo.lower():
                    print(f"Encontrado {mat.titulo} en sucursal {suc.nombre}")
