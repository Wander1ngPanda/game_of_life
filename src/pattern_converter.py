import requests
import sys
import json


url = sys.argv[1]
response = requests.get(url)
grid_array = [line for line in response.text.split('\n') if not line.startswith('!')]
x = len(grid_array[0])
y = len(grid_array)

coord_grid = {}

x_count = 0
y_count = 0

for line in grid_array:
    for item in line:
        coord_grid[(x_count, y_count)] = item == 'O'
        x_count += 1
    x_count = 0
    y_count += 1

alive = set([coord for coord in coord_grid if coord_grid[coord]])


path = 'presets/patterns/'
file_name = url.split('/')[-1].split('.')[0]
full_path = path + file_name + '.json'
data = {'pattern_name': file_name, 'width': x, 'height': y, 'cell_size': 20, 'ruleset': 'default.json', 'coordinates': [list(coord) for coord in alive]}
with open(full_path, 'w') as o:
    json.dump(data, o)
