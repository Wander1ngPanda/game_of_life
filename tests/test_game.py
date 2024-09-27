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