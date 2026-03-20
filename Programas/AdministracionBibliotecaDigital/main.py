from models import *
from datetime import date, timedelta

def ejecutar_pruebas():
    print("PRUEBAS - BIBLIOTECA 'PROGRAVANZADA'")

    #10 LIBROS
    libros = [
        Libro(101, "",0000,"","",""),
        Libro(102, "",0000,"","",""),
        Libro(103, "",0000,"","",""),
        Libro(104, "",0000,"","",""),
        Libro(105, "",0000,"","",""),
        Libro(106, "",0000,"","",""),
        Libro(107, "",0000,"","",""),
        Libro(108, "",0000,"","",""),
        Libro(109, "",0000,"","",""),
        Libro(110, "",0000,"","",""),
    ]
    print("\n Libros registrados:")
    for i,j in enumerate(libros):
        print(f"Libro {i+1}: {j.titulo} |Autor:{j.autor} ({j.añoPublicacion}) |Genero:{j.genero} |ISBN:{j.isbn}")

    #10 REVISTAS
    revistas = [
        Revista(201, "",0000,00,""),
        Revista(202, "",0000,00,""),
        Revista(203, "",0000,00,""),
        Revista(204, "",0000,00,""),
        Revista(205, "",0000,00,""),
        Revista(206, "",0000,00,""),
        Revista(207, "",0000,00,""),
        Revista(208, "",0000,00,""),
        Revista(209, "",0000,00,""),
        Revista(210, "",0000,00,""),
    ]
    print("\n Libros registrados:")
    for i,j in enumerate(libros):
        print(f"Revista {i+1}: {j.titulo} ({j.añoPublicacion})|Edicion:{j.edicion} |Periodicidad:{j.periodicidad}")
    
    #10 MATERIALES DIGITALES
    materiales_digitales = [
        MaterialDigital(301, "",0000,"","",0.0),
        MaterialDigital(302, "",0000,"","",0.0),
        MaterialDigital(303, "",0000,"","",0.0),
        MaterialDigital(304, "",0000,"","",0.0),
        MaterialDigital(305, "",0000,"","",0.0),
        MaterialDigital(306, "",0000,"","",0.0),
        MaterialDigital(307, "",0000,"","",0.0),
        MaterialDigital(308, "",0000,"","",0.0),
        MaterialDigital(309, "",0000,"","",0.0),
        MaterialDigital(310, "",0000,"","",0.0),
    ]
    print("\n Materiales digitales registrados:")
    for i,j in enumerate(materiales_digitales):
        print(f"Material digital {i+1}: {j.titulo} ({j.añoPublicacion})|Tipo de archivo:{j.tipoArchivo} |Tamaño:{j.tamañoMB} MB")

    #10 USUARIOS
    usuarios = [
        Usuario(401, "Juan Perez", 3),
        Usuario(402, "Maria Perez", 3),
        Usuario(403, "Pedro Perez", 3),
        Usuario(404, "Luis Perez", 3),
        Usuario(405, "Carlos Perez", 3),
        Usuario(406, "Manuel Perez", 3),
        Usuario(407, "Juan Perez", 3),
        Usuario(408, "Maria Perez", 3),
        Usuario(409, "Pedro Perez", 3),
        Usuario(410, "Luis Perez", 3),
    ]
    print("\n Usuarios registrados:")
    for i,j in enumerate(usuarios):
        print(f"Usuario {i+1}: {j.nombre} |Limite de prestamos:{j.limitePrestamos}")

    #PRUEBAS
    #BIBLIOTECARIO Y SEDES
    bibliotecario = Bibliotecario(501, "Juan Perez")
    sede_norte = Sucursal(601, "Sede Norte")
    sede_centro = Sucursal(602, "Sede Centro")
    sede_sur = Sucursal(603, "Sede Sur")

    #INGRESAR MATERIAL A SEDE NORTE
    for m in libros + revistas + materiales_digitales:
        sede_norte.catalogoLocal.append(m)

    #PRUEBA PRÉSTAMO
    print("\n>>>PRÉSTAMOS")
    usuario_test = usuarios[0]
    material_test = libros[0]
    print(f"Solicitando: {material_test.titulo} para {usuario_test.nombre}")
    bibliotecario.gestionarPrestamo(usuario_test, material_test)
    print(f"Préstamo exitoso: {material_test.titulo}")

    #PRUEBA TRANSFERENCIA ENTRE SEDES
    print("\n>>>TRANSFERIR MATERIAL")
    material_transf = revistas[0]
    bibliotecario.transferirMaterial(material_transf, sede_centro)
    print(f"Título {material_transf.titulo} transferido con éxito a {sede_centro.nombre}")

    #PRUEBA PENALIZACIONES
    print("\n>>>PENALIZACIONES")
    multa = Penalizacion(100, "Prueba de multa")
    monto = multa.clacularMulta(7)
    print(f"Motivo: {multa.motivo} |Monto: ${monto}")
    multa.bloquearUsuario(usuario_test)

    #RETOS
    print("\n>>>RETOS")
    buscador = Catalogo([sede_norte, sede_centro, sede_sur])

    print(f"BUSCANDO LIBROS DE 'Gabriel García Marquez'")
    resultados = buscador.buscarPorAutor("Gabriel García Marquez")
    for r in resultados:
        print(f"Encontrado {r.titulo} en {sede_norte.nombre}")
        print(f"Título: {r.titulo} |Autor: {r.autor} |Año: {r.añoPublicacion} |Genero: {r.genero} |ISBN: {r.isbn}")

    print(f"BUSCANDO TÉRMINO 'Quijote' EN TODOS LOS SEDES")
    buscador.buscarEnTodasSucursales("Quijote")

if __name__ == "__main__":
    ejecutar_pruebas()