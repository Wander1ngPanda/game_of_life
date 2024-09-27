from game import Game
from ui import UI
from setup import Setup

def main():
    setup = Setup()
    x, y, cell_size = setup.get_input_dimensions()    
    UI(Game(x, y, []), cell_size, 'default.json')

main()
        



    
