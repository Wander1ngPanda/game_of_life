import time
from game import Game
import os

def print_grid(grid):
    row = []
    for coord in grid.keys():
       row.append("⬜" if grid[coord] else "⬛")
       if len(row) == 10:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            row.clear()
    time.sleep(0.1)
    print('\x1b[H')

game = Game(10, 10)

print_grid(game.grid)

game.set_conditions([(0, 0), (0, 1), (0, 2), (1, 2), (2, 1)])

print_grid(game.grid)

try:
    while True:
        game.grid_tick()
        print_grid(game.grid)
except KeyboardInterrupt as e:
    print('Exiting...')
    os.system('cls')

    
    






        



    
