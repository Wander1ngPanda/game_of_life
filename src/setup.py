import tkinter as tk
from tkinter import ttk
from src.presets import Presets
import os


class Setup():
    def __init__(self):
        setup_window = tk.Tk()
        self.presets = Presets()
        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.cell_size = tk.StringVar()
        self.pattern = tk.StringVar()

        dim_label = tk.Label(setup_window, text='What size game')
        x_label = tk.Label(setup_window, text='Width')
        y_label = tk.Label(setup_window, text='Height')
        cell_label = tk.Label(setup_window, text='Cell Size')
        x_input = tk.Entry(setup_window, textvariable=self.x)
        y_input = tk.Entry(setup_window, textvariable=self.y)
        cell_size_input = tk.Entry(setup_window, textvariable=self.cell_size)
        start_button = tk.Button(setup_window, text='Start', command=setup_window.destroy)

        dim_label.grid(row=0, column=0)
        x_label.grid(row=1, column=0)
        x_input.grid(row=1, column=1)
        y_label.grid(row=2, column=0)
        y_input.grid(row=2, column=1)
        cell_label.grid(row=3, column=0)
        cell_size_input.grid(row=3, column=1)
        start_button.grid(row=4, columnspan=2)

        setup_window.mainloop()

    def get_input_dimensions(self):
        try:
            x = int(self.x.get())
        except ValueError as ve:
            x = 40
        try:
            y = int(self.y.get())
        except ValueError as ve:
            y = 30
        try:
            cell_size = int(self.cell_size.get())
        except ValueError as ve:
            cell_size = 20

        return (x, y, cell_size)

    

    
    


    