import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("Estado","Te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("Estado","Te gustan los burritos")
    elif var.get()==3:
        messagebox.showinfo("Estado","Te gusta el sushi")
    elif var.get()==4:
        messagebox.showinfo("Estado","Te gusta la pizza")
    else:
        messagebox.showinfo("Estado","No has elegido ninguna opción")

ven1 = tk.Tk()
ven1.title("Uso del radiobutton")
ven1.geometry("500x500")
ven1.config(bg="#C5D9EC")

etiqueta1=tk.Label(ven1,text="Aquí pondré un radiobutton")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rb1=tk.Radiobutton(ven1,text="Tacos",variable=var,value=1)
rb1.pack(pady=10)
rb2=tk.Radiobutton(ven1,text="Burritos",variable=var,value=2)
rb2.pack(pady=10)
rb3=tk.Radiobutton(ven1,text="Sushi",variable=var,value=3)
rb3.pack(pady=10)
rb4=tk.Radiobutton(ven1,text="Pizza",variable=var,value=4)
rb4.pack(pady=10)

boton1=tk.Button(ven1,text="Verificar opción",command=opcion)
boton1.pack(pady=30)

ven1.mainloop()