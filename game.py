from itertools import product

class Game():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = self.create_grid()
        self.ruleset = {0: False, 1: False, 2: None, 3: True, 4: False, 5: False, 6: False, 7: False, 8: False}
    
    def create_grid(self):
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
        
        x_range = list(range(self.x))
        y_range = list(range(self.y))
        grid = {}
        for coord in product(x_range, y_range):
            grid[coord] = False

        return grid
    
    def get_neighbours(self, coord):
        x, y = coord
        neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), 
                (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        output = []
        for (x, y) in neighbours:
            if x == self.x:
                x = 0
            if x < 0:
                x = self.x -1
            if y == self.y:
                y = 0
            if y < 0:
                y = self.y -1
            output.append((x, y))
        return output
    
    def set_conditions(self, coords):
        for coord in coords:
            self.grid[coord] = True
    
    def cell_tick(self, coord):
        neighbours = self.get_neighbours(coord)
        alive_count = 0
        for value in neighbours:
            if self.grid[value]:
                alive_count += 1
        
        return self.ruleset[alive_count]
    
    def grid_tick(self):
        next_frame = {}
        for coord in self.grid.keys():
            status = self.cell_tick(coord)
            if status != None:
                next_frame[coord] = status
            else:
                next_frame[coord] = self.grid[coord]
        self.grid = next_frame
