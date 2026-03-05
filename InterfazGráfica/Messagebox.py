import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("Ventana de información","Acá puedes escribir info al usuario")
    elif var.get()==2:
        messagebox.showwarning("Ventana de advertencia","Esta es una advertencia")
    elif var.get()==3:
        messagebox.showerror("Ventana de error","Esta es una advertencia")
    elif var.get()==4:
        respuesta=messagebox.askyesno("Ventana de opción","¿Te gusta esta clase?")
        if respuesta:
            messagebox.showinfo("Ventana de info","Más te vale")
        else:
            messagebox.showinfo("Ventana de info","Por eso vas a reprobar")
    elif var.get()==5:
        respuesta2=messagebox.askokcancel("Ventana de opción","Das tu alma a esta clase?")
        if respuesta2:
            messagebox.showinfo("Ventana de info","Por eso vas a sacar 10")
        else:
            messagebox.showinfo("Ventana de info","Por eso repruebas")
    else:
        messagebox.showinfo("Estado","No elegiste nadota")

ven1 = tk.Tk()
ven1.title("Uso de las ventanas de mensaje")
ven1.geometry("500x500")
ven1.config(bg="#C5D9EC")

etiqueta1=tk.Label(ven1,text="Selecciona una opción")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rb1=tk.Radiobutton(ven1,text="Información",variable=var,value=1)
rb1.pack(pady=10)
rb2=tk.Radiobutton(ven1,text="Advertencia",variable=var,value=2)
rb2.pack(pady=10)
rb3=tk.Radiobutton(ven1,text="Error",variable=var,value=3)
rb3.pack(pady=10)
rb4=tk.Radiobutton(ven1,text="Confirmación",variable=var,value=4)
rb4.pack(pady=10)
rb5=tk.Radiobutton(ven1,text="Confirmación",variable=var,value=5)
rb5.pack(pady=10)

boton1=tk.Button(ven1,text="Mostrar ventana",command=opcion)
boton1.pack(pady=30)

ven1.mainloop()