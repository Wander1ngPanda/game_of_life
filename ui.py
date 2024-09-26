import tkinter as tk
from tkinter import ttk
from presets import Presets
import os


class UI():
    def __init__(self, game, cell_size):
        #Useful Variables
        self.X = game.x
        self.Y = game.y
        self.cell_size = cell_size
        self.game = game
        self.game_loop = None
        self.selecting = False
        self.informed = False
        self.presets = Presets()

        #UI Architecture - Main Game Window
        self.game_window = tk.Tk()
        self.game_window.title("Conway's Game of Life")

        #UI Architecture - Control Panel
        self.controller_window = tk.Toplevel(self.game_window)
        self.ruleset_options = tk.StringVar()
        self.speed_value = tk.StringVar()
        self.speed_value.set("50")
        self.speed = int(self.speed_value.get())
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

        self.game_speed_label = tk.Label(self.controller_window, text='Game Speed').pack()
        self.game_speed_entry = tk.Entry(self.controller_window, textvariable=self.speed_value).pack()


        self.ruleset_label = tk.Label(self.controller_window, text='Ruleset').pack()
        ruleset_dropdown = ttk.Combobox(self.controller_window, textvariable = self.ruleset_options)
        ruleset_dropdown['values'] = tuple(self.get_avaliable_rulesets())
        ruleset_dropdown.pack()
        self.current_ruleset_label = tk.Label(self.controller_window, text='Default')
        self.current_ruleset_label.pack()
        ruleset_dropdown.bind('<<ComboboxSelected>>', self.get_preset_rules)
        


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
            self.game_window.after(1000, self.reset_selecting)
            self.game_window.after(10000, self.reset_informed)
        
    
    def reset_selecting(self):
        self.selecting = False

    def reset_informed(self):
        self.informed = False

    def start_game(self):
        self.game.grid_tick()
        self.draw_grid()
        if self.game_loop:
            self.start_game_button["state"] = "disabled"
        self.game_loop = self.game_window.after(self.speed, self.start_game)

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

    def draw_grid(self, initial=False):
        for coord in self.game.tick_scope:
            cell = self.game.grid[coord]
            if coord in self.game.alive:
                self.game_canvas.itemconfig(cell, fill='white')
            else:
                self.game_canvas.itemconfig(cell, fill='black')
                
    def get_preset_rules(self, event):
        try:
            self.presets.parse_rules(self.ruleset_options.get())
            parsed_ruleset = {}
            rule_name = self.presets.rules['title']
            ruleset = self.presets.rules['ruleset']
            for key in ruleset:
                parsed_ruleset[int(key)] = ruleset[key]
            self.game.ruleset = parsed_ruleset
            self.current_ruleset_label.config(text=rule_name)
            print(self.game.ruleset)
        except PermissionError as pe:
            return False

    def get_avaliable_rulesets(self):
        return os.listdir('presets/rules/')
