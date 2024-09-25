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
        self.ruleset = tk.StringVar()


        title = tk.Label(setup_window, text='Conway''s Game of Life')
        dim_label = tk.Label(setup_window, text='What size game')
        x_label = tk.Label(setup_window, text='Width')
        y_label = tk.Label(setup_window, text='Height')
        cell_label = tk.Label(setup_window, text='Cell Size')
        x_input = tk.Entry(setup_window, textvariable=self.x)
        y_input = tk.Entry(setup_window, textvariable=self.y)
        cell_size_input = tk.Entry(setup_window, textvariable=self.cell_size)
        ruleset_label = tk.Label(setup_window, text='Ruleset')
        ruleset_dropdown = ttk.Combobox(setup_window, textvariable = self.ruleset) 
        ruleset_dropdown['values'] = tuple(self.get_avaliable_rulesets())
        ruleset_dropdown.current(0)

        start_button = tk.Button(setup_window, text='Start', command=setup_window.destroy)

        for item in [title, dim_label, x_label, y_label, cell_label, x_input, y_input, cell_size_input, start_button, ruleset_label, ruleset_dropdown]:
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
    
    def get_preset_rules(self):
        self.presets.parse_rules(self.ruleset.get())
        parsed_ruleset = {}
        ruleset = self.presets.rules['ruleset']
        for key in ruleset:
            parsed_ruleset[int(key)] = ruleset[key]
        return parsed_ruleset
    
    def get_avaliable_rulesets(self):
        return os.listdir('presets/rules/')


    