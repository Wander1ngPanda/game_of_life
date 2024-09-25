from game import Game
from ui import UI
from setup import Setup
import tkinter as tk

def main():
    setup = Setup()
    x, y, cell_size = setup.get_dimensions()
    UI(Game(x, y), cell_size)

main()
        



    
