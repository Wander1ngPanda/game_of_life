from itertools import product
from pprint import pprint

class Game():
    def __init__(self, x, y, ruleset, pattern):
        self.x = x
        self.y = y
        self.grid = self.create_grid()
        self.tick_scope = set()
        if ruleset:
            self.ruleset = ruleset
        else:
            self.ruleset = {0: False, 1: False, 2: None, 3: True, 4: False, 5: False, 6: False, 7: False, 8: False}
        if pattern:
            self.alive = set(pattern)
        else:
            self.alive = set()
    
    def create_grid(self):
        x_range = list(range(self.x))
        y_range = list(range(self.y))
        grid = {}
        for coord in product(x_range, y_range):
            grid[coord] = None
        return grid
    

    #! Implement a switch to turn on or off world wrapping
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
    
    def make_alive(self, coords):
        for coord in coords:
            self.alive.add(coord)
    
    def cell_tick(self, coord):
        neighbours = self.get_neighbours(coord)
        alive_count = 0
        for value in neighbours:
            if value in self.alive:
                alive_count += 1
        
        return self.ruleset[alive_count]
    
    def grid_tick(self):
        self.set_scope()
        alive = set()
        for coord in self.tick_scope:
            status = self.cell_tick(coord)
            if status != None or (status == None and coord in self.alive):
                if status or status == None:
                    alive.add(coord)
        self.alive = alive
        
    def set_scope(self):
        self.tick_scope.clear()
        for coord in self.alive:
            self.tick_scope.add(coord)
            for neighbour in self.get_neighbours(coord):
                self.tick_scope.add(neighbour)

    def update_rules(self):
        pass
