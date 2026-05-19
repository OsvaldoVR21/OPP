# Comedor Universitario

Sistema de Gestión de Comedor Universitario desarrollado en Python con interfaz gráfica, utilizando Tkinter y CustomTkinter.

El sistema permite administrar usuarios, inventario, pedidos y carrito de compras mediante distintos paneles para clientes y empleados.

---

# Características

## 👤 Usuarios

* Inicio de sesión
* Registro de clientes
* Roles de usuario:

  * Cliente
  * Empleado
  * Administrador

## Pedidos

* Carrito de compras
* Confirmación de pedidos
* Seguimiento de estado:

  * Pendiente
  * Preparando
  * Listo
  * Entregado
  * Cancelado

## Inventario

* Registro de productos
* Control de stock
* Edición y eliminación de productos
* Búsqueda y filtrado

## Interfaz gráfica

* Diseño con CustomTkinter
* Treeviews personalizados
* Ventanas modales
* Paneles dinámicos

## Persistencia de datos

La información se almacena utilizando archivos CSV:

* usuarios.csv
* productos.csv
* pedidos.csv

---

# Tecnologías utilizadas

* Python
* Tkinter
* CustomTkinter
* CSV
* ttk

---

# Estructura del proyecto

```txt id="l0ib7d"
ComedorUNI/
│
├── backend.py
├── frontend.py
├── usuarios.csv
├── productos.csv
├── pedidos.csv
└── README.md
```

---

# Ejecución del proyecto

## 1. Clonar el repositorio

```bash id="0rw9ax"
git https://github.com/OsvaldoVR21/OPP/tree/main/ComedorUniversitario
```

## 2. Entrar a la carpeta

```bash id="xwx4a7"
cd Comedor Universitario
```

## 3. Instalar dependencias

```bash id="k5i68o"
pip install customtkinter
```

## 4. Ejecutar el sistema

```bash id="f7gxpk"
python frontend.py
```

---

# Credenciales de prueba

## Administrador

```txt id="jknjbh"
Correo: admin@comedor.com
Contraseña: admin123
```

## Cocinero

```txt id="55l2zw"
Correo: cocina@comedor.com
Contraseña: cocina123
```

## Cliente

```txt id="k9z0r9"
Correo: alumno@comedor.com
Contraseña: alumno123
```

---

# Capturas
Login 



