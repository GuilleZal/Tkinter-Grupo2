import tkinter as tk
from tkinter import messagebox
import json
import os

# FUNCIONES
def agregar_gasto():

    global total 

    var_desc = Descrip_caja.get()
    monto_texto = Monto_caja.get()

    try:
        var_monto = float(monto_texto)
    except ValueError:
        messagebox.showerror("Error de Monto", "El monto debe ser un número.")
        return

    if var_desc and var_monto >= 0:
        Lista_gastos.insert(tk.END, f"{var_desc}:   ${var_monto}")
        Descrip_caja.delete(0, tk.END)
        Monto_caja.delete(0, tk.END)
        total += var_monto
        Total_label.config(text= f"Total: {total}")


def eliminar_gasto():

    global total
    seleccion = Lista_gastos.curselection() #Guardo en una variable el gasto que selecciono el usuario
    if seleccion: #Si es verdadero entonces
        texto = Lista_gastos.get(seleccion) # Obtengo la descripcion y monto que selecciono el usuario
        monto = float(texto.split('$')[-1]) 
        """ La funcion split separa el string cada vez que encuentra el caracter "$" y devuelve 
        una lista en la cual solicita el ultimo elemento, osea el monto."""
        total -= monto #Descuento del total
        Total_label.config(text= f"Total: {total}") # Muestro en el label total
        Lista_gastos.delete(seleccion) #Elimina el gasto de la lista

# Creo la ventana tkinter
ventana = tk.Tk()
ventana.title('Calculadora de Gastos')
ventana.geometry('300x400')

#Etiqueta o label de descripcion
Descrip_texto = tk.Label(ventana, text="Ingrese la descripción:")
Descrip_texto.pack()

#Caja de texto de descripcion
Descrip_caja = tk.Entry(ventana)
Descrip_caja.pack()

#Etiqueta o label de monto
Monto = tk.Label(ventana, text="Ingrese el monto:")
Monto.pack()

#Caja de texto del monto
Monto_caja = tk.Entry(ventana)
Monto_caja.pack()

#Etiqueta o label de la lista
Lista_label = tk.Label(ventana, text="Lista de gastos")
Lista_label.pack()

#Creo la lista
Lista_gastos = tk.Listbox(ventana)
Lista_gastos.pack()

total = 0 # Inicializo la variable total 

#Etiqueta o label del total
Total_label = tk.Label(ventana, text = f"Total: {total} ")
Total_label.pack()

# BOTONES
Boton_agregar = tk.Button(ventana, text= "Agregar gasto", command=agregar_gasto)
Boton_agregar.pack(pady=10)

Boton_eliminar = tk.Button(ventana, text = "Eliminar gasto", command=eliminar_gasto)
Boton_eliminar.pack()


ventana.mainloop()


