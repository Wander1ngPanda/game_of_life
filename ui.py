from pprint import pprint
import tkinter as tk

class UI():
    def __init__(self, game, cell_size):
        self.X = game.x
        self.Y = game.y
        self.cell_size = cell_size
        self.game = game

        self.game_window = tk.Tk()
        self.game_window.title("Conway's Game of Life")

        self.controller_window = tk.Toplevel(self.game_window)
        self.controller_window.transient(self.game_window)
        self.controller_window.title('Controls')
        
        self.controller_canvas = tk.Canvas(self.controller_window)
        self.start_game_button = tk.Button(self.controller_window, text='Play', command=self.start_game)
        self.start_game_button.pack()

        self.pause_game_button = tk.Button(self.controller_window, text='Pause', command=self.pause_game)
        self.pause_game_button.pack()

        self.game_canvas = tk.Canvas(self.game_window, width=self.X * self.cell_size, height=self.Y * self.cell_size)
        for coord in self.game.grid.keys():
            x, y = coord
            self.game.grid[coord]['cell'] = self.game_canvas.create_rectangle(
                                                                    x*self.cell_size,
                                                                    y*self.cell_size,
                                                                    x*self.cell_size + self.cell_size,
                                                                    y*self.cell_size + self.cell_size,
                                                                    fill="black",
                                                                    outline="white"
                                                                    )
            self.game_canvas.tag_bind(self.game.grid[coord]['cell'], "<Button-1>", self.on_click)
        self.game_canvas.pack()
        self.game_window.mainloop()

    
    def get_coords(self, x, y):
        return (x//self.cell_size, y//self.cell_size)
    
    def on_click(self, event):
        x, y = self.get_coords(event.x, event.y)
        cell = self.game.grid[(x, y)]
        if cell['alive']:
            self.game_canvas.itemconfig(cell['cell'], fill='black')
        else:
            self.game_canvas.itemconfig(cell['cell'], fill='white')
        cell['alive'] = not cell['alive']

    def start_game(self):
        self.game.grid_tick()
        for coord in self.game.grid:
            cell = self.game.grid[coord]
            if cell['alive']:
                self.game_canvas.itemconfig(cell['cell'], fill='white')
            else:
                self.game_canvas.itemconfig(cell['cell'], fill='black')
        self.game_window.after(50, self.start_game)


    def pause_game(self):
        print('Trying to pause')

    def reset(self):
        pass
