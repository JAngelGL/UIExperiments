import tkinter as tk
from tkinter import ttk

def on_tab_change(event):
    selected_tab = tab_control.index(tab_control.select())
    print(f"Selected Tab: {selected_tab}")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Dos Pestañas")

# Crear un controlador de pestañas
tab_control = ttk.Notebook(root)

# Pestaña 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Pestaña 1')
label1 = tk.Label(tab1, text='Contenido de la Pestaña 1')
label1.pack(padx=10, pady=10)

# Pestaña 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Pestaña 2')
label2 = tk.Label(tab2, text='Contenido de la Pestaña 2')
label2.pack(padx=10, pady=10)

# Asignar el evento de cambio de pestaña
tab_control.bind('<<NotebookTabChanged>>', on_tab_change)

# Pack the tab control to make it visible
tab_control.pack(expand=1, fill="both")

# Iniciar el bucle principal
root.mainloop()

