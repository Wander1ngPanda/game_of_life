from game import Game
from ui import UI
from setup import Setup
import tkinter as tk

def main():
    setup = Setup()
    x, y, cell_size = setup.get_input_dimensions()
    ruleset = setup.get_preset_rules()
    UI(Game(x, y, ruleset=ruleset), cell_size)

main()
        



    
