import tkinter as tk
from tkinter import filedialog, ttk
import os

class InterfazArchivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleccionar Archivos")

        # Create tabs
        self.tabControl = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Archivos")
        self.tabControl.add(self.tab2, text="Otra Pestaña")
        self.tabControl.pack(expand=1, fill="both")

        self.archivo1 = None
        self.archivo2 = None

        self.lbl_estado = tk.Label(self.tab1, text="Esperando archivos")
        self.lbl_estado.pack()

        self.lbl_archivo1 = tk.Label(self.tab1, text="Ruta Archivo 1:")
        self.lbl_archivo1.pack()

        self.btn_seleccionar1 = tk.Button(self.tab1, text="Seleccionar Archivo 1", command=self.seleccionar_archivo1)
        self.btn_seleccionar1.pack(pady=10)

        self.lbl_archivo2 = tk.Label(self.tab1, text="Ruta Archivo 2:")
        self.lbl_archivo2.pack()

        self.btn_seleccionar2 = tk.Button(self.tab1, text="Seleccionar Archivo 2", command=self.seleccionar_archivo2)
        self.btn_seleccionar2.pack(pady=10)

        self.btn_comparar = tk.Button(self.tab1, text="Comparar", command=self.mam_function)
        self.btn_comparar.pack(pady=10)

        self.lbl_resultado = tk.Label(self.tab1, text="")
        self.lbl_resultado.pack(pady=10)

        # Botones para abrir los archivos
        self.btn_abrir1 = tk.Button(self.tab1, text="Abrir Archivo 1", command=self.abrir_archivo1)
        self.btn_abrir1.pack(pady=10)

        self.btn_abrir2 = tk.Button(self.tab1, text="Abrir Archivo 2", command=self.abrir_archivo2)
        self.btn_abrir2.pack(pady=10)

        self.btn_cerrar = tk.Button(self.tab1, text="Cerrar", command=root.quit)
        self.btn_cerrar.pack(pady=20)

        # Buttons for the second tab
        self.btn_pepe = tk.Button(self.tab2, text="Pepe", command=self.pepe_function)
        self.btn_pepe.pack(pady=10)

    def seleccionar_archivo1(self):
        self.archivo1 = filedialog.askopenfilename(title="Seleccionar Archivo 1")
        self.lbl_archivo1.config(text=f"Ruta Archivo 1: {self.archivo1}")
        self.actualizar_estado()

    def seleccionar_archivo2(self):
        self.archivo2 = filedialog.askopenfilename(title="Seleccionar Archivo 2")
        self.lbl_archivo2.config(text=f"Ruta Archivo 2: {self.archivo2}")
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.archivo1 is not None and self.archivo2 is not None:
            self.lbl_estado.config(text="Archivos listos")
        else:
            self.lbl_estado.config(text="Esperando archivos")

    def mam_function(self):
        if self.archivo1 is not None and self.archivo2 is not None:
            resultado = funcion_externa(self.archivo1, self.archivo2)
            self.lbl_resultado.config(text=resultado)
        else:
            self.lbl_estado.config(text="Esperando archivos")

    def abrir_archivo1(self):
        if self.archivo1 is not None:
            os.system(f"start {self.archivo1}")

    def abrir_archivo2(self):
        if self.archivo2 is not None:
            os.system(f"start {self.archivo2}")

    def pepe_function(self):
        print("Hola, soy Pepe!")

# Función externa que realiza alguna operación con las rutas de los archivos
def funcion_externa(ruta_archivo1, ruta_archivo2):
    print("Ruta Archivo 1:", ruta_archivo1)
    print("Ruta Archivo 2:", ruta_archivo2)
    return "Operación externa realizada"

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazArchivos(root)
    root.mainloop()



