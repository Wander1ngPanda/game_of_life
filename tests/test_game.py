from src.game import Game

def test_create_grid():
    game = Game(10, 10, [])
    grid = game.create_grid()
    assert len(grid) == 100
    assert grid[(0, 0)] == None
    assert grid[(9, 9)] == None

def test_get_neighbours():
    game = Game(10, 10, [])
    neighbours = game.get_neighbours((0, 0))
    assert len(neighbours) == 8
    assert (0, 1) in neighbours
    assert (1, 1) in neighbours
    assert (1, 0) in neighbours
    assert (9, 9) in neighbours
    assert (9, 0) in neighbours
    assert (9, 1) in neighbours
    assert (0, 9) in neighbours
    assert (1, 9) in neighbours

def test_make_alive():
    game = Game(10, 10, [])
    game.make_alive([(0, 0), (1, 1), (2, 2)])
    assert (0, 0) in game.alive
    assert (1, 1) in game.alive
    assert (2, 2) in game.alive

def test_cell_tick():
    game = Game(10, 10, [(0, 1), (1, 1), (2, 1)])
    assert game.cell_tick((0, 1)) == False
    assert game.cell_tick((1, 1)) == None
    assert game.cell_tick((0, 0)) == None
    assert game.cell_tick((1, 0)) == True

def test_grid_tick():
    game = Game(10, 10, [(0, 1), (1, 1), (2, 1)])
    game.grid_tick()
    assert (1, 0) in game.alive
    assert (1, 1) in game.alive
    assert (1, 2) in game.alive
    assert (0, 1) not in game.alive
    assert (2, 1) not in game.alive