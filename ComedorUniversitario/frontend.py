import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from backend import *

# ==========================================
# CONFIGURACIÓN GLOBAL Y ESTADO
# ==========================================
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

auth_sys = SistemaAutenticacion()
inv_sys = SistemaInventario()
ped_sys = SistemaPedidos()

# Estilo para los Treeview en modo oscuro
def configurar_estilos():
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", 
                    background="#2b2b2b", 
                    foreground="white", 
                    rowheight=25, 
                    fieldbackground="#2b2b2b", 
                    borderwidth=0)
    style.configure("Treeview.Heading", 
                    background="#1f1f1f", 
                    foreground="white", 
                    relief="flat", 
                    font=('Arial', 10, 'bold'))
    style.map('Treeview', background=[('selected', '#1f538d')])

def limpiar_pantalla(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

# ==========================================
# PANTALLA: LOGIN Y REGISTRO
# ==========================================
def mostrar_login(ventana):
    limpiar_pantalla(ventana)
    
    frame = ctk.CTkFrame(ventana)
    frame.pack(pady=40, padx=40, fill="both", expand=True)
    
    lbl_titulo = ctk.CTkLabel(frame, text="Sistema Comedor Universitario BUAP", font=("Arial", 24, "bold"))
    lbl_titulo.pack(pady=20)
    
    entry_user = ctk.CTkEntry(frame, placeholder_text="Usuario")
    entry_user.pack(pady=10, padx=20)
    
    entry_pass = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*")
    entry_pass.pack(pady=10, padx=20)
    
    def intentar_login():
        u = entry_user.get()
        p = entry_pass.get()
        usuario = auth_sys.login(u, p)
        if usuario:
            if usuario.rol == "empleado":
                mostrar_pantalla_empleado(ventana, usuario)
            else:
                mostrar_pantalla_cliente(ventana, usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            
    btn_login = ctk.CTkButton(frame, text="Iniciar Sesión", command=intentar_login)
    btn_login.pack(pady=20)

    # Registro rápido para pruebas
    def registrar_cliente():
        auth_sys.registrar("Nuevo Alumno", f"alumno{len(auth_sys.usuarios)}", "123", "cliente")
        messagebox.showinfo("Éxito", "Usuario cliente de prueba creado con éxito.")
        
    btn_reg = ctk.CTkButton(frame, text="Registrar Cliente Prueba", command=registrar_cliente, fg_color="gray")
    btn_reg.pack(pady=10)

# ==========================================
# PANTALLA: CLIENTE
# ==========================================
def mostrar_pantalla_cliente(ventana, usuario):
    limpiar_pantalla(ventana)
    carrito = {} # {id_producto: cantidad}

    header = ctk.CTkFrame(ventana)
    header.pack(fill="x", padx=10, pady=10)
    ctk.CTkLabel(header, text=f"Bienvenido, {usuario.nombre} | Rol: Cliente", font=("Arial", 16)).pack(side="left", padx=10)
    ctk.CTkButton(header, text="Cerrar Sesión", command=lambda: mostrar_login(ventana), fg_color="red").pack(side="right", padx=10)

    tabs = ctk.CTkTabview(ventana)
    tabs.pack(fill="both", expand=True, padx=10, pady=10)
    tab_menu = tabs.add("Menú y Pedidos")
    tab_mis_pedidos = tabs.add("Mis Pedidos")

    # --- PESTAÑA MENÚ ---
    col_izq = ctk.CTkFrame(tab_menu)
    col_izq.pack(side="left", fill="both", expand=True, padx=5)
    col_der = ctk.CTkFrame(tab_menu, width=250)
    col_der.pack(side="right", fill="y", padx=5)

    ctk.CTkLabel(col_izq, text="Menú Disponible", font=("Arial", 14, "bold")).pack(pady=5)
    
    tv_menu = ttk.Treeview(col_izq, columns=("ID", "Nombre", "Tipo", "Precio", "Disp"), show="headings")
    tv_menu.heading("ID", text="ID")
    tv_menu.heading("Nombre", text="Nombre")
    tv_menu.heading("Tipo", text="Tipo")
    tv_menu.heading("Precio", text="Precio ($)")
    tv_menu.heading("Disp", text="Disponible")
    tv_menu.column("ID", width=30)
    tv_menu.pack(fill="both", expand=True, pady=5)

    def refrescar_menu():
        for item in tv_menu.get_children():
            tv_menu.delete(item)
        for p in inv_sys.productos:
            if p.stock > 0:
                tv_menu.insert("", "end", values=(p.id_producto, p.nombre, p.tipo, p.precio, p.stock))
                
    refrescar_menu()

    lbl_carrito = ctk.CTkLabel(col_der, text="Carrito: $0.0", font=("Arial", 14, "bold"))
    lbl_carrito.pack(pady=10)
    
    lista_carrito = tk.Listbox(col_der, bg="#2b2b2b", fg="white", selectbackground="#1f538d")
    lista_carrito.pack(fill="both", expand=True, pady=5)

    def agregar_al_carrito():
        seleccion = tv_menu.selection()
        if not seleccion: return
        item = tv_menu.item(seleccion[0])
        id_prod = str(item['values'][0])
        prod = inv_sys.obtener_producto(id_prod)
        
        if prod:
            carrito[id_prod] = carrito.get(id_prod, 0) + 1
            if carrito[id_prod] > prod.stock:
                messagebox.showwarning("Stock", "No hay más stock disponible.")
                carrito[id_prod] -= 1
            actualizar_ui_carrito()

    def actualizar_ui_carrito():
        lista_carrito.delete(0, tk.END)
        total = 0
        for id_p, cant in carrito.items():
            prod = inv_sys.obtener_producto(id_p)
            lista_carrito.insert(tk.END, f"{cant}x {prod.nombre} - ${prod.precio*cant}")
            total += prod.precio * cant
        lbl_carrito.configure(text=f"Total: ${total:.2f}")

    def confirmar_pedido():
        if not carrito: return
        if ped_sys.crear_pedido(usuario.id_usuario, carrito, inv_sys):
            messagebox.showinfo("Éxito", "Pedido realizado")
            carrito.clear()
            actualizar_ui_carrito()
            refrescar_menu()
            refrescar_mis_pedidos()
        else:
            messagebox.showerror("Error", "No se pudo procesar el pedido.")

    ctk.CTkButton(col_izq, text="Agregar al Carrito ->", command=agregar_al_carrito).pack(pady=10)
    ctk.CTkButton(col_der, text="Confirmar Pedido", command=confirmar_pedido, fg_color="green").pack(pady=10)
    ctk.CTkButton(col_der, text="Limpiar Carrito", command=lambda: [carrito.clear(), actualizar_ui_carrito()]).pack(pady=5)

    # --- PESTAÑA MIS PEDIDOS ---
    tv_mis_ped = ttk.Treeview(tab_mis_pedidos, columns=("ID", "Fecha", "Total", "Estado"), show="headings")
    tv_mis_ped.heading("ID", text="Folio")
    tv_mis_ped.heading("Fecha", text="Fecha")
    tv_mis_ped.heading("Total", text="Total")
    tv_mis_ped.heading("Estado", text="Estado")
    tv_mis_ped.pack(fill="both", expand=True, pady=10)

    def refrescar_mis_pedidos():
        for item in tv_mis_ped.get_children():
            tv_mis_ped.delete(item)
        mis_pedidos = ped_sys.get_pedidos_cliente(usuario.id_usuario)
        for p in mis_pedidos:
            tv_mis_ped.insert("", "end", values=(p.id_pedido, p.fecha, f"${p.total}", p.estado))

    def cancelar_pedido():
        sel = tv_mis_ped.selection()
        if not sel: return
        item = tv_mis_ped.item(sel[0])
        if item['values'][3] == "Pendiente":
            ped_sys.actualizar_estado(item['values'][0], "Cancelado")
            refrescar_mis_pedidos()
        else:
            messagebox.showwarning("Atención", "Solo puedes cancelar pedidos pendientes.")

    ctk.CTkButton(tab_mis_pedidos, text="Cancelar Pedido Seleccionado", command=cancelar_pedido, fg_color="red").pack(pady=10)
    refrescar_mis_pedidos()


# ==========================================
# PANTALLA: EMPLEADO (ADMIN)
# ==========================================
def mostrar_pantalla_empleado(ventana, usuario):
    limpiar_pantalla(ventana)

    header = ctk.CTkFrame(ventana)
    header.pack(fill="x", padx=10, pady=10)
    ctk.CTkLabel(header, text=f"Administración | {usuario.nombre}", font=("Arial", 16)).pack(side="left", padx=10)
    ctk.CTkButton(header, text="Cerrar Sesión", command=lambda: mostrar_login(ventana), fg_color="red").pack(side="right", padx=10)

    tabs = ctk.CTkTabview(ventana)
    tabs.pack(fill="both", expand=True, padx=10, pady=10)
    tab_pedidos = tabs.add("Gestión de Pedidos")
    tab_inv = tabs.add("Inventario (CRUD)")

    # --- PESTAÑA GESTIÓN PEDIDOS ---
    tv_ped = ttk.Treeview(tab_pedidos, columns=("ID", "Cliente", "Total", "Estado", "Fecha"), show="headings")
    for col in ("ID", "Cliente", "Total", "Estado", "Fecha"):
        tv_ped.heading(col, text=col)
    tv_ped.pack(fill="both", expand=True, pady=10)

    def refrescar_pedidos_admin():
        for item in tv_ped.get_children():
            tv_ped.delete(item)
        for p in ped_sys.pedidos:
            tv_ped.insert("", "end", values=(p.id_pedido, p.id_cliente, f"${p.total}", p.estado, p.fecha))

    def avanzar_estado():
        sel = tv_ped.selection()
        if not sel: return
        id_ped = str(tv_ped.item(sel[0])['values'][0])
        estado_actual = tv_ped.item(sel[0])['values'][3]
        
        nuevo_estado = "Pendiente"
        if estado_actual == "Pendiente": nuevo_estado = "Preparando"
        elif estado_actual == "Preparando": nuevo_estado = "Entregado"
        elif estado_actual == "Cancelado" or estado_actual == "Entregado": return
        
        ped_sys.actualizar_estado(id_ped, nuevo_estado)
        refrescar_pedidos_admin()

    ctk.CTkButton(tab_pedidos, text="Avanzar Estado (Pend -> Prep -> Entr)", command=avanzar_estado).pack(pady=10)
    refrescar_pedidos_admin()

    # --- PESTAÑA INVENTARIO (CRUD) ---
    tv_inv = ttk.Treeview(tab_inv, columns=("ID", "Nombre", "Tipo", "Precio", "Stock"), show="headings")
    for col in ("ID", "Nombre", "Tipo", "Precio", "Stock"):
        tv_inv.heading(col, text=col)
    tv_inv.pack(fill="both", expand=True, pady=10)

    def refrescar_inventario():
        for item in tv_inv.get_children():
            tv_inv.delete(item)
        for p in inv_sys.productos:
            tv_inv.insert("", "end", values=(p.id_producto, p.nombre, p.tipo, p.precio, p.stock))

    def abrir_modal_producto(id_editar=None):
        modal = ctk.CTkToplevel(ventana)
        modal.title("Gestión de Producto")
        modal.geometry("300x350")
        modal.grab_set() # Deshabilita ventana principal
        
        ctk.CTkLabel(modal, text="Nombre:").pack(pady=(10,0))
        ent_nombre = ctk.CTkEntry(modal)
        ent_nombre.pack()
        
        ctk.CTkLabel(modal, text="Tipo:").pack(pady=(10,0))
        ent_tipo = ctk.CTkEntry(modal)
        ent_tipo.pack()
        
        ctk.CTkLabel(modal, text="Precio:").pack(pady=(10,0))
        ent_precio = ctk.CTkEntry(modal)
        ent_precio.pack()
        
        ctk.CTkLabel(modal, text="Stock:").pack(pady=(10,0))
        ent_stock = ctk.CTkEntry(modal)
        ent_stock.pack()

        if id_editar:
            p = inv_sys.obtener_producto(id_editar)
            ent_nombre.insert(0, p.nombre)
            ent_tipo.insert(0, p.tipo)
            ent_precio.insert(0, str(p.precio))
            ent_stock.insert(0, str(p.stock))

        def guardar():
            try:
                nom = ent_nombre.get()
                tipo = ent_tipo.get()
                pre = float(ent_precio.get())
                stk = int(ent_stock.get())
                
                if id_editar:
                    inv_sys.editar_producto(id_editar, nom, tipo, pre, stk)
                else:
                    inv_sys.agregar_producto(nom, tipo, pre, stk)
                    
                refrescar_inventario()
                modal.destroy()
            except ValueError:
                messagebox.showerror("Error", "Precio o Stock inválidos")

        ctk.CTkButton(modal, text="Guardar", command=guardar).pack(pady=20)

    def eliminar_seleccionado():
        sel = tv_inv.selection()
        if not sel: return
        id_prod = str(tv_inv.item(sel[0])['values'][0])
        inv_sys.eliminar_producto(id_prod)
        refrescar_inventario()

    def editar_seleccionado():
        sel = tv_inv.selection()
        if not sel: return
        id_prod = str(tv_inv.item(sel[0])['values'][0])
        abrir_modal_producto(id_prod)

    frame_btns = ctk.CTkFrame(tab_inv)
    frame_btns.pack(fill="x", pady=10)
    ctk.CTkButton(frame_btns, text="Agregar", command=lambda: abrir_modal_producto()).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(frame_btns, text="Editar", command=editar_seleccionado).pack(side="left", expand=True, padx=5)
    ctk.CTkButton(frame_btns, text="Eliminar", fg_color="red", command=eliminar_seleccionado).pack(side="left", expand=True, padx=5)
    
    refrescar_inventario()


# ==========================================
# INICIO DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Sistema de Gestión de Comedor")
    app.geometry("800x600")
    configurar_estilos()
    mostrar_login(app)
    app.mainloop()