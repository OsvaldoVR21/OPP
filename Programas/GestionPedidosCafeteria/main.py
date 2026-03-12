from models import *
from datetime import datetime

def ejecutar_pruebas():
    print("PRUEBAS - CAFETERIA 'PROGRAVANZADA COFFEE' ")

#10 CLIENTES
    clientes = [
        Cliente(1, "Elizabeht Gutierrez", "lizygr@gmail.com"),
        Cliente(2, "Amy Fuentes", "amyfuentes08@gmail.com"),
        Cliente(3, "Marco Serrano", "marcoserranoavi@gmail.com"),
        Cliente(4, "Odalys Hernandez", "odalysshh@gmail.com"),
        Cliente(5, "Mery Lopez", "meryjane222@gmail.com"),
        Cliente(6,"Gustavo Vázquez", "gustavovax22@gmail.com"),
        Cliente(7, "Leonardo Romero", "leonardorom22@gmail.com"),
        Cliente(8, "Jesús Roque", "jesusroqueh@gmail.com"),
        Cliente(9, "Isaí Vázquez", "isaivr21@gmail.com"),
        Cliente(10, "Yukari Rosas", "yukissr@gmail.com"),
    ]

    print("\n Clientes registrados:")
    for i, c in enumerate(clientes):
        print(f"Cliente {i+1}: {c.nombre} ({c.email})")

#10 BEBIDAS
    bebidas =[
        Bebida(201, "Americano", 30.0, "Grande", Temperatura.CALIENTE),
        Bebida(202, "Chocomilk", 25.0, "Grande", Temperatura.FRIA),
        Bebida(203, "Capuccino", 50.0, "Grande", Temperatura.CALIENTE),
        Bebida(204, "Moka", 45.0, "Grande", Temperatura.CALIENTE),
        Bebida(205, "Latte", 55.0, "Grande", Temperatura.CALIENTE),
        Bebida(206, "Choco Latte", 40.0, "Grande", Temperatura.CALIENTE),
        Bebida(207, "Frapuccino", 50.0, "Grande", Temperatura.FRIA),
        Bebida(208, "Abuelita", 25.0, "Grande", Temperatura.CALIENTE),
        Bebida(209, "Chocotavo", 15.0, "Grande", Temperatura.FRIA),
        Bebida(210, "Espresso", 35.0, "Grande", Temperatura.CALIENTE),
    ]
    
    print("\n\n BEBIDAS")
    for i, b in enumerate(bebidas):
        print(f"Bebida {i+1}: {b.nombre} ({b.temperatura.value})")

#10 EMPLEADOS
    empleados = [
        Empleado(101, "Empleado 1", "empleadofulanito1.cafeprogra@gmail.com", "E-001", Rol.GERENTE),
        Empleado(102, "Empleado 2", "empleadofulanito2.cafeprogra@gmail.com", "E-002", Rol.BARISTA),
        Empleado(103, "Empleado 3", "empleadofulanito3.cafeprogra@gmail.com", "E-003", Rol.BARISTA),
        Empleado(104, "Empleado 4", "empleadofulanito4.cafeprogra@gmail.com", "E-004", Rol.BARISTA),
        Empleado(105, "Empleado 5", "empleadofulanito5.cafeprogra@gmail.com", "E-005", Rol.BARISTA),
        Empleado(106, "Empleado 6", "empleadofulanito6.cafeprogra@gmail.com", "E-006", Rol.MESERO),
        Empleado(107, "Empleado 7", "empleadofulanito7.cafeprogra@gmail.com", "E-007", Rol.MESERO),
        Empleado(108, "Empleado 8", "empleadofulanito8.cafeprogra@gmail.com", "E-008", Rol.MESERO),
        Empleado(109, "Empleado 9", "empleadofulanito9.cafeprogra@gmail.com", "E-009", Rol.MESERO),
        Empleado(110, "Empleado 10", "empleadofulanito10.cafeprogra@gmail.com", "E-010", Rol.MESERO),
    ]

    print("\n\n EMPLEADOS")
    for i, e in enumerate(empleados):
        print(f"Empleado {i+1}: {e.nombre} ({e.email}) - {e.rol.value}")

#LOGIN
    print("\n\n PRUEBA DE LOGIN")
    for e in empleados:
        e.login()

#PERFILES
    print("\n\n PRUEBA DE PERFILES")
    for e in clientes:
        e.actualizarPerfil()

#PRUEBA PRODUCTOS
    print("\n\n PRUEBA DE PRODUCTOS")
    test_bebida = bebidas[0]
    print(f"Bebida: {test_bebida.nombre} \n Precio base: ${test_bebida.precioBase}")
    test_bebida.agregarExtra("Leche de Almendra")
    test_bebida.agregarExtra("Shot de café")
    print(f"Extras: {test_bebida.modificadores}")
    print(f"Precio final: ${test_bebida.calcularPrecioFinal()}")

#RETO: flujo de pedido e inventario
    print("\n\n >>>Proceso de venta. . . ")
    Inventario_barra = Inventario()

    Inventario_barra.ingredientes["café"] = 0

    usuario_actual = clientes[0]
    pedido_actual = Pedido(5001)

    print(f"Cliente: {usuario_actual.nombre} \n Puntos de fidelidad ({usuario_actual.puntosFidelidad})")
    print(f"Atiente: {empleados[1].nombre} (BARISTA)" )

    pedido_actual.productos.append(bebidas[0])
    print(f"[SISTEMA]: Agregando {bebidas[0].nombre} al pedido. . .")

    print(f"[SISTEMA]: Verificando disponibilidad de stock. . .")
    if Inventario_barra.ingredientes["café"] <= 0:
        print(f"[ERROR]: STOCK INSUFICIENTE")
        
        empleados[1].actualizarInventario()
        Inventario_barra.ingredientes["café"] = 50
        print(f"[SISTEMA]: Inventario actualizado. Procediendo con pedido. . .")


    empleados[1].cambiarEstadoPedido(pedido_actual, Estado.PREPARADO)
    Inventario_barra.reducirStock("café", 2)

#RESUMEN
    print("\n\n >>> RESUMEN DE VENTA")
    monto_final = pedido_actual.calcularTotal()
    print(f"Usuario: {usuario_actual.nombre}")
    print(f"Productos: {[p.nombre for p in pedido_actual.productos]}")
    print(f"Total: ${monto_final}")

    empleados[1].cambiarEstadoPedido(pedido_actual, Estado.ENTREGADO)
    usuario_actual.realizarPedido(pedido_actual)
    usuario_actual.puntosFidelidad +=10

    print("\n\n >>> VALIDACION DE DATOS")
    print(f"Estado Final del pedido {pedido_actual.idPedido}: {pedido_actual.estado.value}")
    print(f"Puntos fidelidad del cliente {usuario_actual.nombre}: {usuario_actual.puntosFidelidad}")

if __name__ == "__main__":
    ejecutar_pruebas()