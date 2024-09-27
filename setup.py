import tkinter as tk
from tkinter import ttk
from presets import Presets
import os


class Setup():
    def __init__(self):
        setup_window = tk.Tk()
        self.presets = Presets()
        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.cell_size = tk.StringVar()
        self.pattern = tk.StringVar()


        title = tk.Label(setup_window, text='Conway''s Game of Life')
        dim_label = tk.Label(setup_window, text='What size game')
        x_label = tk.Label(setup_window, text='Width')
        y_label = tk.Label(setup_window, text='Height')
        cell_label = tk.Label(setup_window, text='Cell Size')
        x_input = tk.Entry(setup_window, textvariable=self.x)
        y_input = tk.Entry(setup_window, textvariable=self.y)
        cell_size_input = tk.Entry(setup_window, textvariable=self.cell_size)
        
        start_button = tk.Button(setup_window, text='Start', command=setup_window.destroy)

        for item in [title, dim_label, x_label, y_label, cell_label, x_input, y_input, cell_size_input, start_button]:
            item.pack()
        
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

    

    
    


    