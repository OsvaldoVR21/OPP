import tkinter as tk 
from PIL import ImageTk, Image

def nuevo_archivo():
    messagebox.showinfo("Información","Creaste un nuevo archivo")

def abrir_archivo():
    messagebox.showinfo("Información","Abriste un archivo")

def guardar_archivo():
    messagebox.showinfo("Información","Guardaste un archivo")

def cortar_a():
    messagebox.showinfo("Información","Cortaste un texto")

def pegar_a():
    messagebox.showinfo("Información","Pegaste un texto")

ven1 = tk.Tk()
ven1.title("Ventana de menú")
ven1.geometry("500x500")
ven1.config(bg="#C5D9EC")

barra_menu = tk.Menu(ven1)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo archivo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir archivo", command=abrir_archivo)
menu_archivo.add_command(label="Guardar archivo", command=guardar_archivo)

menu_edicion = tk.Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar_a)
menu_edicion.add_command(label="Pegar", command=pegar_a)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)

ven1.config(menu=barra_menu)

ven1.mainloop()