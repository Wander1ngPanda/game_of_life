from itertools import product
from pprint import pprint

#This is the ruleset for the game of life
#All Corresponding boolean row are what a cell with the corresponding alive cells next to it will become for the next game tick
#If the number of neighbours is less than 2 it dies. Seen here by the cell becoming false
#If the number of neighbours is equal to 2 then it survives. Seen here by None. It should not change.
#If the number of neighbours is equal to 3 then it becomes alive. Seen here by True.
#If the number of neighbours is greater than 3 then it should die. Seen here by False.
RULESET = {0: False, 1: False, 2: None, 3: True, 4: False, 5: False, 6: False, 7: False, 8: False}
X = 10
Y = 10

#! Note: Grid and X and Y is being passed around a lot.
#! Might be better to make it a class and pass it around that way.
#! Or get it from the largest coord in Grid

def create_grid(x, y):
    """
    Creates a grid for the Game of Life.
    Args:
        x (int): The number of columns in the grid.
        y (int): The number of rows in the grid.
    Returns:
        dict: A dictionary representing the grid, where each key is a tuple 
              (row, column) and the value is a boolean indicating whether 
              the cell is alive (True) or dead (False).
    """
    
    x_range = list(range(x))
    y_range = list(range(y))
    grid = {}
    for coord in product(x_range, y_range):
        grid[coord] = False

    return grid

def get_neighbours(coord, x_bounds, y_bounds):
    x, y = coord
    neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), 
            (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    output = []
    for (x, y) in neighbours:
        if x == x_bounds:
            x = 0
        if x < 0:
            x = x_bounds -1
        if y == y_bounds:
            y = 0
        if y < 0:
            y = y_bounds -1
        output.append((x, y))
    return output

def set_conditions(grid, coords):
    for coord in coords:
        grid[coord] = True
    return grid


def cell_tick(coord, x_bound, y_bound, grid):
    neighbours = get_neighbours(coord, x_bound, y_bound)
    alive_count = 0
    for value in neighbours:
        if grid[value]:
            alive_count += 1
    
    return RULESET[alive_count]

def grid_tick(grid):
    next_frame = {}
    for coord in grid.keys():
        status = cell_tick(coord, X, Y, grid)
        if status != None:
            next_frame[coord] = status
        else:
            next_frame[coord] = grid[coord]
    return next_frame

def print_grid(grid):
    row = []
    for coord in grid.keys():
       row.append("⬜" if grid[coord] else "⬛")
       if len(row) == 10:
            print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            row.clear()
    print("-" * 20)



grid = create_grid(X, Y)

print_grid(grid)

set_conditions(grid, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 1)])

print_grid(grid)


while True:
    grid = grid_tick(grid)

    print_grid(grid)






        



    
