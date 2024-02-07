import tkinter as tk
from tkinter import filedialog
import os

class FileSelector:
    def __init__(self, master, file_paths=None):
        self.master = master
        master.title("File Selector")

        self.file_path_1 = tk.StringVar()
        self.file_path_2 = tk.StringVar()
        self.done_message = tk.StringVar()

        tk.Label(master, text="File 1:").pack()
        self.file_button_1 = tk.Button(master, text="Select", command=self.select_file_1)
        self.file_button_1.pack()
        self.file_entry_1 = tk.Entry(master, textvariable=self.file_path_1, state="readonly")
        self.file_entry_1.pack()

        tk.Label(master, text="File 2:").pack()
        self.file_button_2 = tk.Button(master, text="Select", command=self.select_file_2)
        self.file_button_2.pack()
        self.file_entry_2 = tk.Entry(master, textvariable=self.file_path_2, state="readonly")
        self.file_entry_2.pack()

        tk.Button(master, text="Done", command=self.show_done_message).pack()
        tk.Label(master, textvariable=self.done_message, font=("Arial", 12), fg="green").pack()

        self.route_open_func_1 = None
        self.route_open_func_2 = None

        if file_paths is not None and len(file_paths) >= 1:
            self.file_path_1.set(file_paths[0])
            self.route_open_func_1 = self.open_document_1

        tk.Button(master, text="Open File 1", command=self.open_file_1).pack()
        tk.Button(master, text="Open File 2", command=self.open_file_2).pack()

    def select_file_1(self):
        file_path = filedialog.askopenfilename()
        self.file_path_1.set(file_path)

    def select_file_2(self):
        file_path = filedialog.askopenfilename()
        self.file_path_2.set(file_path)

    def show_done_message(self):
        self.done_message.set("Done!")

    def open_document_1(self):
        os.startfile(self.file_path_1.get())

    def open_file_1(self):
        if self.route_open_func_1 is not None:
            self.route_open_func_1()

    def open_file_2(self):
        if self.route_open_func_2 is not None:
            self.route_open_func_2()

root = tk.Tk()
file_paths = ["C:\\Users\\angel\\Workspace\\Libro1.xlsx", "C:\\Users\\angel\\Workspace\\Libro1 copy.xlsx"]
app = FileSelector(root, file_paths)
root.mainloop()
