import tkinter as tk
from tkinter import messagebox


# --- Mensajes y colores dinámicos ---
mensajes = [
    "hola profe", 
    "como estas?", 
    "le gusta el codigo?", 
    "pongame un 5 porfa jeje", 
    "con mucho cariño y respeto, juan manuel londoño rios"
]
indice_mensaje = 0

colores = ["red", "green", "blue", "purple", "orange"]
indice_color = 0

# --- Funciones para botones ---
def cambiar_texto():
    global indice_mensaje
    etiqueta_derecha.config(text=mensajes[indice_mensaje])
    indice_mensaje = (indice_mensaje + 1) % len(mensajes)
def cambiar_color():
    global indice_color
    etiqueta_derecha.config(fg=colores[indice_color])
    indice_color = (indice_color + 1) % len(colores)

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "gracias por decidir usar mi app ;)")

# --- Funciones para menú ---
def mostrar_tutorial():
    messagebox.showinfo("Tutorial", "Esta aplicación te ayuda a practicar Tkinter.\nUsa los botones para interactuar con los marcos.")

def salir_aplicacion():
    ventana.destroy()

def funcionalidad_1():
    messagebox.showinfo("Funcionalidad 1", "El botón 'Cambiar texto' modifica el texto dinámicamente.")

def funcionalidad_2():
    messagebox.showinfo("Funcionalidad 2", "El botón 'Cambiar color' cambia el color del texto principal.")

def acerca_de():
    messagebox.showinfo("Acerca de", "Autor: Juan Manuel Londoño Rios\n\nAplicación de práctica con Tkinter.")

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Aplicación Tkinter")

# Icono de la ventana
try:
    ventana.iconbitmap("icono.ico")
except:
    print("icono.ico")

ventana.geometry("600x400")

# --- Menú ---
menu_principal = tk.Menu(ventana)

# Menú Inicio
menu_inicio = tk.Menu(menu_principal, tearoff=0)
menu_inicio.add_command(label="Tutorial de la aplicación", command=mostrar_tutorial)
menu_inicio.add_separator()
menu_inicio.add_command(label="Salir", command=salir_aplicacion)
menu_principal.add_cascade(label="Inicio", menu=menu_inicio)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_ayuda.add_command(label="Funcionalidad 1", command=funcionalidad_1)
menu_ayuda.add_command(label="Funcionalidad 2", command=funcionalidad_2)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)

# Menú Acerca de
menu_principal.add_command(label="Acerca de", command=acerca_de)

# Asignar menú a la ventana
ventana.config(menu=menu_principal)

# --- Marcos ---
marco_izquierdo = tk.Frame(ventana, width=200, bg="lightgray")
marco_izquierdo.pack(side="left", fill="y")

marco_derecho = tk.Frame(ventana, bg="white")
marco_derecho.pack(side="right", expand=True, fill="both")

# --- Elementos del marco izquierdo ---
etiqueta_info = tk.Label(marco_izquierdo, text="Opciones de la aplicación:", bg="lightgray", font=("Arial", 12))
etiqueta_info.pack(pady=10)

boton1 = tk.Button(marco_izquierdo, text="Cambiar texto", command=cambiar_texto)
boton1.pack(pady=5, padx=10, fill="x")

boton2 = tk.Button(marco_izquierdo, text="Cambiar color", command=cambiar_color)
boton2.pack(pady=5, padx=10, fill="x")

boton3 = tk.Button(marco_izquierdo, text="Mostrar mensaje", command=mostrar_mensaje)
boton3.pack(pady=5, padx=10, fill="x")

# --- Elemento del marco derecho ---
etiqueta_derecha = tk.Label(marco_derecho, text="Bienvenido a la aplicación", font=("Arial", 16), bg="white", fg="black")
etiqueta_derecha.pack(expand=True)

# --- Iniciar la app ---
ventana.mainloop()