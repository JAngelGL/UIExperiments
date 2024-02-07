import tkinter as tk
from tkinter import filedialog

class InterfazArchivos:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleccionar Archivos")

        self.archivo1 = None
        self.archivo2 = None

        self.lbl_estado = tk.Label(root, text="Esperando archivos")
        self.lbl_estado.pack()

        self.lbl_archivo1 = tk.Label(root, text="Ruta Archivo 1:")
        self.lbl_archivo1.pack()

        self.btn_seleccionar1 = tk.Button(root, text="Seleccionar Archivo 1", command=self.seleccionar_archivo1)
        self.btn_seleccionar1.pack(pady=10)

        self.lbl_archivo2 = tk.Label(root, text="Ruta Archivo 2:")
        self.lbl_archivo2.pack()

        self.btn_seleccionar2 = tk.Button(root, text="Seleccionar Archivo 2", command=self.seleccionar_archivo2)
        self.btn_seleccionar2.pack(pady=10)

        self.btn_comparar = tk.Button(root, text="Comparar", command=self.mam_function)
        self.btn_comparar.pack(pady=10)

        self.lbl_resultado = tk.Label(root, text="")
        self.lbl_resultado.pack(pady=10)

        self.btn_cerrar = tk.Button(root, text="Cerrar", command=root.quit)
        self.btn_cerrar.pack(pady=20)

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
            # Aquí puedes agregar tu lógica y series de instrucciones
            # Ejemplo: realizar alguna comparación o procesamiento con los archivos seleccionados
            self.lbl_resultado.config(text="Done")
        else:
            self.lbl_estado.config(text="Esperando archivos")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazArchivos(root)
    root.mainloop()
