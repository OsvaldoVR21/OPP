import csv
import os
import datetime

# ==========================================
# MODELOS (ENTIDADES)
# ==========================================
class Usuario:
    def __init__(self, id_usuario, nombre, username, password, rol):
        self.id_usuario = str(id_usuario)
        self.nombre = nombre
        self.username = username
        self.password = password
        self.rol = rol

class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, username, password):
        super().__init__(id_usuario, nombre, username, password, "cliente")

class Empleado(Usuario):
    def __init__(self, id_usuario, nombre, username, password):
        super().__init__(id_usuario, nombre, username, password, "empleado")

class Producto:
    def __init__(self, id_producto, nombre, tipo, precio, stock):
        self.id_producto = str(id_producto)
        self.nombre = nombre
        self.tipo = tipo
        self.precio = float(precio)
        self.stock = int(stock)

class Pedido:
    def __init__(self, id_pedido, id_cliente, lista_productos, total, estado, fecha=None):
        self.id_pedido = str(id_pedido)
        self.id_cliente = str(id_cliente)
        self.lista_productos = lista_productos # Formato: "id1:cant,id2:cant"
        self.total = float(total)
        self.estado = estado # Pendiente, Preparando, Entregado, Cancelado
        self.fecha = fecha if fecha else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ==========================================
# CONTROLADORES (SISTEMAS)
# ==========================================
class SistemaAutenticacion:
    def __init__(self):
        self.archivo = 'usuarios.csv'
        self.usuarios = []
        self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            # Usuario administrador por defecto
            self.usuarios.append(Empleado("1", "Admin Comedor", "admin", "1234"))
            self.actualizar_csv()
            return

        with open(self.archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['rol'] == 'empleado':
                    user = Empleado(row['id'], row['nombre'], row['username'], row['password'])
                else:
                    user = Cliente(row['id'], row['nombre'], row['username'], row['password'])
                self.usuarios.append(user)

    def actualizar_csv(self):
        with open(self.archivo, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "username", "password", "rol"])
            for u in self.usuarios:
                writer.writerow([u.id_usuario, u.nombre, u.username, u.password, u.rol])

    def login(self, username, password):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return u
        return None

    def registrar(self, nombre, username, password, rol="cliente"):
        if any(u.username == username for u in self.usuarios):
            return False # Username ya existe
        nuevo_id = str(len(self.usuarios) + 1)
        if rol == "empleado":
            nuevo_user = Empleado(nuevo_id, nombre, username, password)
        else:
            nuevo_user = Cliente(nuevo_id, nombre, username, password)
        self.usuarios.append(nuevo_user)
        self.actualizar_csv()
        return True

class SistemaInventario:
    def __init__(self):
        self.archivo = 'productos.csv'
        self.productos = []
        self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            # Productos por defecto
            self.productos = [
                Producto("1", "Chilaquiles", "Platillo", 45.0, 20),
                Producto("2", "Agua de Jamaica", "Bebida", 15.0, 50)
            ]
            self.actualizar_csv()
            return

        with open(self.archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.productos.append(Producto(row['id'], row['nombre'], row['tipo'], row['precio'], row['stock']))

    def actualizar_csv(self):
        with open(self.archivo, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "tipo", "precio", "stock"])
            for p in self.productos:
                writer.writerow([p.id_producto, p.nombre, p.tipo, p.precio, p.stock])

    def obtener_producto(self, id_producto):
        for p in self.productos:
            if p.id_producto == str(id_producto):
                return p
        return None

    def agregar_producto(self, nombre, tipo, precio, stock):
        nuevo_id = str(len(self.productos) + 1)
        nuevo_prod = Producto(nuevo_id, nombre, tipo, precio, stock)
        self.productos.append(nuevo_prod)
        self.actualizar_csv()

    def editar_producto(self, id_producto, nombre, tipo, precio, stock):
        prod = self.obtener_producto(id_producto)
        if prod:
            prod.nombre = nombre
            prod.tipo = tipo
            prod.precio = float(precio)
            prod.stock = int(stock)
            self.actualizar_csv()

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != str(id_producto)]
        self.actualizar_csv()

    def disminuir_stock(self, id_producto, cantidad):
        prod = self.obtener_producto(id_producto)
        if prod and prod.stock >= cantidad:
            prod.stock -= cantidad
            self.actualizar_csv()
            return True
        return False

class SistemaPedidos:
    def __init__(self):
        self.archivo = 'pedidos.csv'
        self.pedidos = []
        self._cargar_datos()

    def _cargar_datos(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.pedidos.append(Pedido(row['id'], row['id_cliente'], row['lista_productos'], row['total'], row['estado'], row['fecha']))

    def actualizar_csv(self):
        with open(self.archivo, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "id_cliente", "lista_productos", "total", "estado", "fecha"])
            for p in self.pedidos:
                writer.writerow([p.id_pedido, p.id_cliente, p.lista_productos, p.total, p.estado, p.fecha])

    def crear_pedido(self, id_cliente, carrito, sis_inventario):
        # Carrito es un diccionario {id_producto: cantidad}
        total = 0.0
        lista_prod_str = []
        
        for id_prod, cant in carrito.items():
            prod = sis_inventario.obtener_producto(id_prod)
            if prod and prod.stock >= cant:
                total += prod.precio * cant
                lista_prod_str.append(f"{id_prod}:{cant}")
                sis_inventario.disminuir_stock(id_prod, cant)
        
        if total > 0:
            nuevo_id = str(len(self.pedidos) + 1)
            str_productos = ",".join(lista_prod_str)
            nuevo_pedido = Pedido(nuevo_id, id_cliente, str_productos, total, "Pendiente")
            self.pedidos.append(nuevo_pedido)
            self.actualizar_csv()
            return True
        return False

    def actualizar_estado(self, id_pedido, nuevo_estado):
        for p in self.pedidos:
            if p.id_pedido == str(id_pedido):
                p.estado = nuevo_estado
                self.actualizar_csv()
                break

    def get_pedidos_cliente(self, id_cliente):
        return [p for p in self.pedidos if p.id_cliente == str(id_cliente)]