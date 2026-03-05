import tkinter as tk
from PIL import Image, ImageTk
import os

# Obtener ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_IMAGENES = os.path.join(BASE_DIR, "imagenes")

# Variable global para la selección
var = None

def abrir_seleccion():
    seleccion = var.get()
    if seleccion == 1:
        ventana_2()
    elif seleccion == 2:
        ventana_3()
    elif seleccion == 3:
        ventana_4()
    elif seleccion == 4:
        ventana_5()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_principal():
    global vent1, var, img1_tk

    vent1 = tk.Tk()
    vent1.title("Reino Animal")
    vent1.geometry("600x650")
    vent1.config(bg="#708c4c")

    etiq1 = tk.Label(
        vent1,
        text="Reino Animal",
        font=("Georgia", 20, "bold"),
        fg="White",
        bg="#C77140",
        padx=10,
        pady=10
    )
    etiq1.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

    # Imagen portada
    imagen = Image.open(os.path.join(RUTA_IMAGENES, "Animaless.jpg"))
    imagen = imagen.resize((300, 400))
    img1_tk = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(vent1, image=img1_tk)
    label_imagen.grid(row=1, column=0, rowspan=4, padx=5, pady=5)

    var = tk.IntVar(value=0)

    tk.Radiobutton(vent1, text="Jirafa", variable=var, value=1, bg="#667E45").grid(row=1, column=1, sticky="w", padx=5)
    tk.Radiobutton(vent1, text="Elefante", variable=var, value=2, bg="#667E45").grid(row=2, column=1, sticky="w", padx=5)
    tk.Radiobutton(vent1, text="León", variable=var, value=3, bg="#667E45").grid(row=3, column=1, sticky="w", padx=5)
    tk.Radiobutton(vent1, text="Castor", variable=var, value=4, bg="#667E45").grid(row=4, column=1, sticky="w", padx=5)

    boton = tk.Button(
        vent1,
        text="Ir a la opción seleccionada",
        bg="#756859",
        command=abrir_seleccion
    )
    boton.grid(row=5, column=0, columnspan=2, pady=20)

    vent1.mainloop()


def ventana_2():
    global vent2, img2_tk
    vent1.destroy()

    vent2 = tk.Tk()
    vent2.title("Jirafas")
    vent2.geometry("650x600")
    vent2.config(bg="#b1816c")

    img = Image.open(os.path.join(RUTA_IMAGENES, "Jirafaa.jpg"))
    img = img.resize((300, 350))
    img2_tk = ImageTk.PhotoImage(img)

    tk.Label(vent2, text="Las Jirafas", font=("Georgia", 18, "bold"),fg="white", bg="#5B4941").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(vent2, image=img2_tk).grid(row=1, column=1, padx=5, pady=5)

    texto = ("La jirafa es el mamífero terrestre más alto del mundo y habita principalmente en África. Su largo cuello le permite alcanzar hojas de árboles altos, especialmente acacias. Es herbívora y sus manchas son únicas en cada individuo.")

    tk.Label(vent2, text=texto, wraplength=250, justify="left",font=("Arial", 12, "bold"), bg="#6588A9").grid(row=1, column=2, padx=5)

    tk.Button(vent2, text="Regresar", bg="#667E45",command=lambda: regresar_a_primera(vent2),width=15).grid(row=2, column=0, columnspan=2, pady=30)

    vent2.mainloop()


def ventana_3():
    global vent3, img3_tk
    vent1.destroy()

    vent3 = tk.Tk()
    vent3.title("Elefante")
    vent3.geometry("650x600")
    vent3.config(bg="#9A918D")

    img = Image.open(os.path.join(RUTA_IMAGENES, "Elefantee.jpg"))
    img = img.resize((300, 350))
    img3_tk = ImageTk.PhotoImage(img)

    tk.Label(vent3, text="Los Elefantes", font=("Georgia", 18, "bold"),fg="white", bg="#726A77").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(vent3, image=img3_tk).grid(row=1, column=1, padx=5, pady=5)

    texto = ("El elefante africano es el animal terrestre más grande. Vive en África y se alimenta de plantas. Utiliza su trompa para respirar, beber agua y sujetar objetos, y es reconocido por su gran inteligencia.")

    tk.Label(vent3, text=texto, wraplength=250, justify="left",font=("Arial", 12, "bold"), bg="#F2E4D7").grid(row=1, column=2, padx=5)

    tk.Button(vent3, text="Regresar", bg="#667E45",command=lambda: regresar_a_primera(vent3),width=15).grid(row=2, column=1, pady=30)

    vent3.mainloop()


def ventana_4():
    global vent4, img4_tk
    vent1.destroy()

    vent4 = tk.Tk()
    vent4.title("León")
    vent4.geometry("650x600")
    vent4.config(bg="#896859")

    img = Image.open(os.path.join(RUTA_IMAGENES, "Leonn.jpg"))
    img = img.resize((300, 350))
    img4_tk = ImageTk.PhotoImage(img)

    tk.Label(vent4, text="Los Leones", font=("Georgia", 18, "bold"),fg="white", bg="#c77140").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(vent4, image=img4_tk).grid(row=1, column=0, padx=10, pady=5)

    texto = ("El león es un felino carnívoro conocido como el rey de la selva.Vive principalmente en África y se organiza en grupos llamados manadas. Los machos se distinguen por su melena.")

    tk.Label(vent4, text=texto, wraplength=250, justify="left",font=("Arial", 12, "bold"), bg="#b8860b").grid(row=1, column=1, padx=5)

    tk.Button(vent4, text="Regresar", bg="#667E45",command=lambda: regresar_a_primera(vent4),width=20).grid(row=2, column=0, pady=30)

    vent4.mainloop()


def ventana_5():
    global vent5, img5_tk
    vent1.destroy()

    vent5 = tk.Tk()
    vent5.title("Castor")
    vent5.geometry("650x600")
    vent5.config(bg="#a0522d")

    img = Image.open(os.path.join(RUTA_IMAGENES, "castor.jpg"))
    img = img.resize((300, 350))
    img5_tk = ImageTk.PhotoImage(img)

    tk.Label(vent5, text="Los Castores", font=("Georgia", 18, "bold"),fg="white", bg="#955C1F").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(vent5, image=img5_tk).grid(row=1, column=1, padx=5, pady=5)

    texto = ("El castor americano es un roedor semiacuático que habita en América del Norte. Es famoso por construir presas con madera para crear estanques donde vive. Tiene dientes muy fuertes que crecen continuamente.")

    tk.Label(vent5, text=texto, wraplength=250, justify="left",font=("Arial", 12, "bold"), bg="#7d460e").grid(row=1, column=2, padx=5)

    tk.Button(vent5, text="Regresar", bg="#667E45",command=lambda: regresar_a_primera(vent5),width=20).grid(row=2, column=0, columnspan=2, pady=30)

    vent5.mainloop()


# Iniciar programa
ventana_principal()