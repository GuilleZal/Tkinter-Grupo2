import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess

# Ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("600x400")
ventana.resizable(False, False)

# Marco para el formulario
marco_formulario = tk.Frame(ventana, bg='white', bd=2)
marco_formulario.place(relx=0.5, rely=0.5, anchor="center", width=300, height=250)

# Título
etiqueta_titulo = tk.Label(marco_formulario, text="Iniciar Sesión", font=("Helvetica", 16, "bold"), bg="white")
etiqueta_titulo.pack(pady=10)

# Entrada de usuario
entrada_usuario = tk.Entry(marco_formulario, font=("Helvetica", 12), bg="#FADADD")
entrada_usuario.insert(0, "Usuario")
entrada_usuario.pack(pady=5, ipadx=10, ipady=5)

# Entrada de contraseña
entrada_clave = tk.Entry(marco_formulario, show="*", font=("Helvetica", 12), bg="#FADADD")
entrada_clave.insert(0, "Contraseña")
entrada_clave.pack(pady=5, ipadx=10, ipady=5)

# Opciones de recordar y olvido de clave
marco_opciones = tk.Frame(marco_formulario, bg="white")
marco_opciones.pack(pady=5)

recordar_var = tk.IntVar()
check_recordar = tk.Checkbutton(marco_opciones, text="Recordarme", variable=recordar_var, bg="white")
check_recordar.grid(row=0, column=0)

boton_olvido = tk.Button(marco_opciones, text="¿Olvidaste tu contraseña?", bg="white", bd=0, fg="blue")
boton_olvido.grid(row=0, column=1)

# Función para login
def iniciar_sesion():
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()

    if not os.path.exists("usuarios.json"):
        messagebox.showerror("Error", "No hay usuarios registrados.")
        return

    with open("usuarios.json", "r") as f:
        usuarios = json.load(f)

    if usuario in usuarios and usuarios[usuario] == clave:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
        ventana.destroy()

        # Abrir la calculadora de gastos
        subprocess.Popen(["python", "calculadora_de_gastos.py"])
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

# Función para abrir ventana de registro
def abrir_ventana_registro():
    ventana_registro = tk.Toplevel(ventana)
    ventana_registro.title("Crear Cuenta")
    ventana_registro.geometry("300x250")
    ventana_registro.resizable(False, False)

    tk.Label(ventana_registro, text="Nuevo Usuario", font=("Helvetica", 12)).pack(pady=10)
    entry_usuario = tk.Entry(ventana_registro, font=("Helvetica", 12))
    entry_usuario.pack(pady=5)

    tk.Label(ventana_registro, text="Contraseña", font=("Helvetica", 12)).pack()
    entry_clave = tk.Entry(ventana_registro, show="*", font=("Helvetica", 12))
    entry_clave.pack(pady=5)

    def registrar_nuevo_usuario():
        usuario = entry_usuario.get()
        clave = entry_clave.get()

        if not usuario or not clave:
            messagebox.showerror("Error", "Completá usuario y contraseña.")
            return

        if os.path.exists("usuarios.json"):
            with open("usuarios.json", "r") as f:
                usuarios = json.load(f)
        else:
            usuarios = {}

        if usuario in usuarios:
            messagebox.showwarning("Advertencia", "Ese usuario ya existe.")
        else:
            usuarios[usuario] = clave
            with open("usuarios.json", "w") as f:
                json.dump(usuarios, f)
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")
            ventana_registro.destroy()
                # Fin de registrar_nuevo_usuario()
    
    tk.Button(ventana_registro, text="Crear cuenta", command=registrar_nuevo_usuario, bg="#5D3FD3", fg="white").pack(pady=15)


# Botón de iniciar sesión
boton_login = tk.Button(marco_formulario, text="Ingresar", command=iniciar_sesion, bg="#5D3FD3", fg="white", font=("Helvetica", 12))
boton_login.pack(pady=10, ipadx=10, ipady=5)

# Botón para crear cuenta (ACTIVADO)
boton_crear_cuenta = tk.Button(marco_formulario, text="Crear Cuenta", bg="white", fg="blue", bd=0, command=abrir_ventana_registro)
boton_crear_cuenta.pack()

ventana.mainloop()