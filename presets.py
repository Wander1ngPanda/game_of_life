import json

class Presets():
    def __init__(self):
        self.pattern = None
        self.rules = None

    def parse_pattern(self, filename):
        with open(f'presets/patterns/{filename}') as file:
            data = json.load(file)
            self.pattern = data
    
    def parse_rules(self, filename):
        with open(f'presets/rules/{filename}') as file:
            data = json.load(file)
            self.rules = data
    