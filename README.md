# Project: Game of Life

### Notes:

This is a functioning version of the game of life.
It is a little bit buggy and almost entirely untested

The initial screen lets you choose the dimensions and cell size for the game
- The Height and Width is in cells
- The cell_size describes how large each cell should be, 1 is almost invisible, 20 is a nice size

The control panel lets the game run
- Play will run continuously
- Increment will progress the curent generation by one tick
- Pause will stop the game
- Reset will wipe out all alive cells
- Ruleset can be controlled by loading saved json files
- Load preset configurations loads saved json files
- Save allow the current screen to be saved as a json file to be later loaded

### Tests:
- Try to implement Hypothesis
- Need to add unit testing for game.py
    - Game Logic (if one thing is tested it should be this)

### Features to Add
- Keep a count of the generations for each run
- Allow the control of the grid size while it is open

### Current Bugs
- Clicking reset will not work if it hasnt been run
    - Will also brick the window
- X ing the control panel leaves you with no option but to quit and restart
- The file converter will have either the right hand side not filled in or the bottom. Breaks some patterns
    - Not all paterns are designed for a looping world

