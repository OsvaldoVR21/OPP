from models import *
from datetime import date, timedelta

def ejecutar_pruebas():
    print("PRUEBAS - BIBLIOTECA 'PROGRAVANZADA'")

    #10 LIBROS
    libros = [
        Libro(101, "El principito",1943,"Antoine Saint-Exupéry","9780156013987","Fábula"),
        Libro(102, "Bajo la misma estrella",2012,"Jhon Green","9780525478812","Juvenil"),
        Libro(103, "Crepúsculo",2005,"Sthephanie Miller","9780525478812","Fantasía Romántica"),
        Libro(104, "1984",1949,"George Orwell","9780525478812","Distopía"),
        Libro(105, "Cien años de soledad",1998,"Gabriel García Márquez","9780525478812","Realismo mágico"),
        Libro(106, "Don Quijote de la Mancha",1922,"Miguel de Cervantes","9780525478812","Clásico"),
        Libro(107, "El amor en los tiempos del cólera",1985,"Gabriel García Márquez","9780525478812","Ficción"),
        Libro(108, "Crónica de una muerte anunciada",1981,"Gabriel García Márquez","9780525478812","Novela"),
        Libro(109, "El alquimista",1988,"Paulo Coelho","9780525478812","Fición"),
        Libro(110, "El código da vinci",1999,"Dan Brown","9780525478812","Suspenso"),
    ]
    print("\n Libros registrados:")
    for i,j in enumerate(libros):
        print(f"Libro {i+1}: {j.titulo} |Autor:{j.autor} ({j.añoPublicacion}) |Genero:{j.genero} |ISBN:{j.isbn}")

    #10 REVISTAS
    revistas = [
        Revista(201, "Muy interesante",1985,150,"Semanal"), 
        Revista(202, "Forbes",2013,88,"Mensual"),
        Revista(203, "Cosmopolitan",2013,88,"Mensual"),
        Revista(204, "Quién",1999,44,"Mensual"),
        Revista(205, "Expansión",1969,59,"Mensual"),
        Revista(206, "El País",1984,74,"Mensual"),
        Revista(207, "National Geographic",2018,94,"Semanal"),
        Revista(208, "Vanidades",2001,19,"Semanal"),
        Revista(209, "Proceso",2007,98,"Semanal"),
        Revista(210, "TVNotas",2020,63,"Semanal"),
    ]
    print("\n Revistas registradas:")
    for i,j in enumerate(revistas):
        print(f"Revista {i+1}: {j.titulo} ({j.añoPublicacion})|Edicion:{j.edicion} |Periodicidad:{j.periodicidad}")
    
    #10 MATERIALES DIGITALES
    materiales_digitales = [
        MaterialDigital(301, "Python para principiantes",2004,"PDF","https://www.python.org/downloads/release/python-485/",5.1),
        MaterialDigital(302, "Python avanzado",2010,"PDF","https://www.python.org/downloads/release/python-104/",7.1),
        MaterialDigital(303, "Introducción a python",2007,"PDF","https://www.python.org/downloads/release/python-132/",4.1),
        MaterialDigital(304, "Python para principiantes pt.2",2026,"PDF","https://www.python.org/downloads/release/python-942/",5.8),
        MaterialDigital(305, "Python para seniors",2011,"PDF","https://www.python.org/downloads/release/python-872/",9.7),
        MaterialDigital(306, "Cómo enseñarle python a mi bebé pt.1",2025,"PDF","https://www.python.org/downloads/release/python-178/",4.1),
        MaterialDigital(307, "Puede mi gato conocer Python?",2020,"PDF","https://www.python.org/downloads/release/python-892/",1.0),
        MaterialDigital(308, "Python vs Java",2012,"PDF","https://www.python.org/downloads/release/python-189/",2.1),
        MaterialDigital(309, "Cómo enseñarle python a mi bebé pt.2",2017,"PDF","https://www.python.org/downloads/release/python-918/",4.1),
        MaterialDigital(310, "Por qué tengo tantos libros de python?",2015,"PDF","https://www.python.org/downloads/release/python-981/",1.1),
    ]
    print("\n Materiales digitales registrados:")
    for i,j in enumerate(materiales_digitales):
        print(f"Material digital {i+1}: {j.titulo} ({j.añoPublicacion})|Tipo de archivo:{j.tipoArchivo} |Tamaño:{j.tamañoMB} MB")

    #10 USUARIOS
    usuarios = [
        Usuario(401, "Osvaldo Vázquez", 3),
        Usuario(402, "Isaí Romero", 3),
        Usuario(403, "Elizabeth Gutierrez", 3),
        Usuario(404, "Amy Fuentes", 3),
        Usuario(405, "Marco Serrano", 3),
        Usuario(406, "Antonio Aviles", 3),
        Usuario(407, "Yukari Rosas", 3),
        Usuario(408, "Isaac Perez", 3),
        Usuario(409, "Odalys Hernandez", 3),
        Usuario(410, "Mary Sanchez", 3),
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
    monto = multa.calcularMulta(7)
    print(f"Motivo: {multa.motivo} |Monto: ${monto}")
    multa.bloquearUsuario(usuario_test)

    #RETOS
    print("\n>>>RETOS")
    buscador = Catalogo([sede_norte, sede_centro, sede_sur])

    print(f"BUSCANDO LIBROS DE 'Gabriel García Márquez'")
    resultados = buscador.buscarPorAutor("Gabriel García Márquez")
    for r in resultados:
        print(f"\n Encontrado {r.titulo} en {sede_norte.nombre}")
        print(f"Título: {r.titulo} |Autor: {r.autor} |Año: {r.añoPublicacion} |Genero: {r.genero} |ISBN: {r.isbn}")

    print(f"\nBUSCANDO TÉRMINO 'Quijote' EN TODOS LOS SEDES")
    buscador.buscarEnTodasSucursales("Quijote")

if __name__ == "__main__":
    ejecutar_pruebas()