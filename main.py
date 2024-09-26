from game import Game
from ui import UI
from setup import Setup
import tkinter as tk

def main():
    setup = Setup()
    preset_pattern = setup.get_preset_pattern()
    if preset_pattern:
        x, y, cell_size, pattern = preset_pattern
    else:
        x, y, cell_size = setup.get_input_dimensions()
        pattern = False
    ruleset = setup.get_preset_rules()
    
    UI(Game(x, y, ruleset=ruleset, pattern=pattern), cell_size)

main()
        



    
