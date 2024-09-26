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
        pattern_label = tk.Label(setup_window, text='Pattern')
        pattern_dropdown = ttk.Combobox(setup_window, textvariable=self.pattern)
        pattern_dropdown['values'] = tuple(self.get_avaliable_patterns())
        start_button = tk.Button(setup_window, text='Start', command=setup_window.destroy)

        for item in [title, dim_label, x_label, y_label, cell_label, x_input, y_input, cell_size_input, start_button, pattern_label, pattern_dropdown]:
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

    def get_preset_pattern(self):
        try:
            self.presets.parse_pattern(self.pattern.get())
            x = self.presets.pattern['width']
            y = self.presets.pattern['height']
            cell_size = self.presets.pattern['cell_size']
            coordinates = [tuple(coord) for coord in self.presets.pattern['coordinates']]
            return x, y, cell_size, coordinates
        except PermissionError as pe:
            return False

    
    def get_avaliable_patterns(self):
        return os.listdir('presets/patterns/')


    