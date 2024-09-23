import tkinter as tk
from game import Game
X = 100
Y = 50

game = Game(X, Y)


window = tk.Tk()

canvas = tk.Canvas(window, width=X*10, height=Y*10)

for coord in game.grid.keys():
    x, y = coord
    canvas.create_rectangle(x*10, y*10, x*10 + 10, y*10 + 10, fill="black", outline="white")

canvas.pack()

window.mainloop()