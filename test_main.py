from hypothesis import given, settings
from main import create_grid, get_neighbours
from hypothesis.strategies import integers, tuples

coordinate_data = tuples(integers(min_value=1, max_value=2000), integers(min_value=1, max_value=2000))

@settings(max_examples=10, deadline=None)
@given(integers(min_value=1, max_value=2000), integers(min_value=1, max_value=2000))
def test_create_grid_returns_dictionary_of_correct_length(x, y):
    assert len(create_grid(x, y)) == x*y

@settings(max_examples=10, deadline=None)
@given(coordinate_data)
def test_get_neighbours_returns_eight_neighbours(coord):
    assert len(get_neighbours(coord)) == 8


