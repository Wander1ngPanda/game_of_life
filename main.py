from src.game import Game
from src.ui import UI
from src.setup import Setup

def main():
    setup = Setup()
    x, y, cell_size = setup.get_input_dimensions()  
    UI(Game(x, y, []), cell_size, 'default.json')

main()
        



    
