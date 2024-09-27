import tkinter as tk
from tkinter import ttk, simpledialog
from src.presets import Presets
import json
import os
from src.game import Game

class UI():
    def __init__(self, game, cell_size, ruleset_path):
        self.game_window = tk.Tk()

        self.X = game.x
        self.Y = game.y
        self.cell_size = cell_size
        self.game = game
        self.game_loop = None
        self.selecting = False
        self.informed = False
        self.after_ids = []

        self.ruleset_path = ruleset_path
        self.presets = Presets()
        self.presets.parse_rules(ruleset_path)
        self.ruleset_title = self.presets.rules['title']

        self.controller_window = tk.Toplevel(self.game_window)
        self.ruleset_options = tk.StringVar()
        self.pattern_options = tk.StringVar()
        
 
        self.controller_window.transient(self.game_window)
        self.controller_window.title('Controls')
    
        self.start_game_button = tk.Button(self.controller_window, text='Play', command=self.start_game)
        self.start_game_button.pack()

        pause_game_button = tk.Button(self.controller_window, text='Pause', command=self.pause_game)
        pause_game_button.pack()

        self.increment_game_button = tk.Button(self.controller_window, text='Increment', command=self.increment_game)
        self.increment_game_button.pack()

        self.reset_game_button = tk.Button(self.controller_window, text='Reset', command=self.reset_game)
        self.reset_game_button.pack()


        self.ruleset_label = tk.Label(self.controller_window, text='Ruleset').pack()
        ruleset_dropdown = ttk.Combobox(self.controller_window, textvariable = self.ruleset_options)
        ruleset_dropdown['values'] = tuple(self.get_avaliable_rulesets())
        ruleset_dropdown.pack()
        self.current_ruleset_label = tk.Label(self.controller_window, text=self.ruleset_title)
        self.current_ruleset_label.pack()
        ruleset_dropdown.bind('<<ComboboxSelected>>', self.set_preset_rules)

        self.pattern_label = tk.Label(self.controller_window, text='Pattern').pack()
        pattern_dropdown = ttk.Combobox(self.controller_window, textvariable=self.pattern_options)
        pattern_dropdown['values'] = tuple(self.get_avaliable_patterns())
        pattern_dropdown.pack()
        pattern_dropdown.bind('<<ComboboxSelected>>', self.load_pattern)

        tk.Button(self.controller_window, text='Save Current Pattern', command=self.save_file).pack()
        


        self.game_canvas = tk.Canvas(self.game_window, width=self.X * self.cell_size, height=self.Y * self.cell_size)
            
        for coord in self.game.grid.keys():
            x, y = coord
            if coord in self.game.alive:
                fill = 'white'
            else:
                fill = 'black'
            self.game.grid[coord] = self.game_canvas.create_rectangle(
                                                                    x * self.cell_size,
                                                                    y * self.cell_size,
                                                                    x * self.cell_size + self.cell_size,
                                                                    y * self.cell_size + self.cell_size,
                                                                    fill=fill
                                                                    )
            self.game_canvas.tag_bind(self.game.grid[coord], "<B1-Motion>", self.select_cells)
            self.game_canvas.tag_bind(self.game.grid[coord], "<Button-1>", self.select_cells)

        self.game_canvas.pack()
        self.set_preset_rules(ruleset_path)
        self.game_window.mainloop()

    
    def get_coords(self, x, y):
        return (x//self.cell_size, y//self.cell_size)
    
    def select_cells(self, event):
        try:
            x, y = self.get_coords(event.x, event.y)
            cell = self.game.grid[(x, y)]
            if self.selecting != cell:
                self.selecting = cell
                if (x,y) in self.game.alive:
                    self.game_canvas.itemconfig(cell, fill='black')
                    self.game.alive.remove((x, y))
                else:
                    self.game_canvas.itemconfig(cell, fill='white')
                    self.game.alive.add((x, y))
        except KeyError as k:
            if not self.informed:
                print('Have you tried painting between the lines. Keep it in the window')
                self.informed = True

        finally:
            self.after_ids.append(self.game_window.after(1000, self.reset_selecting))
            self.after_ids.append(self.game_window.after(10000, self.reset_informed))
        
    
    def reset_selecting(self):
        self.selecting = False

    def reset_informed(self):
        self.informed = False

    def start_game(self):
        self.game.grid_tick()
        self.draw_grid()
        if self.game_loop:
            self.start_game_button["state"] = "disabled"
        self.game_loop = self.game_window.after(50, self.start_game)
        self.after_ids.append(self.game_loop)

    def pause_game(self):
        if self.game_loop:
            self.game_window.after_cancel(self.game_loop)
            self.game_loop = None
            self.start_game_button["state"] = "active"

    def reset_game(self):
        if self.game_loop:
            self.pause_game()    
        self.game.alive.clear()
        self.draw_grid()

    def increment_game(self):
        self.pause_game()
        self.game.grid_tick()
        self.draw_grid()

    def draw_grid(self):
        for coord in self.game.tick_scope:
            cell = self.game.grid[coord]
            if coord in self.game.alive:
                self.game_canvas.itemconfig(cell, fill='white')
            else:
                self.game_canvas.itemconfig(cell, fill='black')
                
    def set_preset_rules(self, event):
        self.pause_game()
        try:
            if type(event) == str:
                ruleset_options = event
            else:
                ruleset_options = self.ruleset_options.get()
            self.presets.parse_rules(ruleset_options)
            parsed_ruleset = {}
            rule_name = self.presets.rules['title']
            ruleset = self.presets.rules['ruleset']
            for key in ruleset:
                parsed_ruleset[int(key)] = ruleset[key]
            self.game.ruleset = parsed_ruleset
            self.ruleset_path = self.ruleset_options.get()
            self.current_ruleset_label.config(text=rule_name)
        except PermissionError as pe:
            return False

    def get_avaliable_rulesets(self):
        return os.listdir('presets/rules/')
    
    def get_avaliable_patterns(self):
        return os.listdir('presets/patterns/')
    
    def get_game_info(self):
        if not self.ruleset_path:
            self.ruleset_path = 'default.json'
        print(self.ruleset_path)
        return {
            'width': self.X,
            'height': self.Y,
            'cell_size': self.cell_size,
            'ruleset': self.ruleset_path,
            'coordinates': [list(coord) for coord in self.game.alive]
        }
    
    def save_file(self):
        self.pause_game()
        data = self.get_game_info()
        path = 'presets/patterns/'
        file_name = simpledialog.askstring(title='Pattern Title', prompt='Name Pattern:')
        if file_name and file_name not in self.get_avaliable_rulesets() and len(file_name.strip()) > 0:
            data['pattern_name'] = file_name
            full_path = path + file_name + '.json'
            with open(full_path, 'w') as o:
                json.dump(data, o)

    def load_pattern(self, event):
        self.reset_game()
        self.presets.parse_pattern(self.pattern_options.get())
        alive = [tuple(coord) for coord in self.presets.pattern['coordinates']]
        self.set_preset_rules(self.presets.pattern['ruleset'])
        x = self.presets.pattern['width']
        y = self.presets.pattern['height']
        cell_size = self.presets.pattern['cell_size']
        self.safe_destroy()

        #! Ugly
        UI(Game(x, y, alive), cell_size, self.presets.pattern['ruleset'])

    def safe_destroy(self):
        for process in self.after_ids:
            self.game_window.after_cancel(process)
        self.game_window.destroy()

        
        








        

