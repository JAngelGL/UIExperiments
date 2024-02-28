import tkinter as tk
from tkinter import ttk

class VentanaConPestanas:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana con Pestañas")

        # Crear el widget Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)

        # Crear el contenido de la primera pestaña
        self.frame1 = ttk.Frame(self.notebook)
        self.label1 = ttk.Label(self.frame1, text="Contenido de la Pestaña 1")
        self.label1.pack(padx=10, pady=10)
        self.notebook.add(self.frame1, text="Pestaña 1")

        # Crear el contenido de la segunda pestaña
        self.frame2 = ttk.Frame(self.notebook)
        self.label2 = ttk.Label(self.frame2, text="Contenido de la Pestaña 2")
        self.label2.pack(padx=10, pady=10)
        self.notebook.add(self.frame2, text="Pestaña 2")

        # Empaquetar el widget Notebook en la ventana
        self.notebook.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    ventana = VentanaConPestanas(root)
    root.mainloop()

