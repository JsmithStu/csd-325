"""Forest Fire Sim, modified by Johnathan Smith for CSD-325 Module 6
A simulation of wildfires spreading in a forest with a central lake.
The lake is blue, uses a different character, cannot be modified,
and acts as a firebreak that flames cannot cross.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '

# NEW: water feature constants
WATER = '~'          # must not be A or @
WATER_COLOR = 'blue' # displayed in blue

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01           # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01           # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


# NEW ---------------------------------------------------------
def is_lake_cell(x, y):
    """Return True if this (x, y) coordinate is inside the central lake.

    The lake is a rectangle roughly centered in the display and will be
    filled with WATER cells that never change and block fire spread.
    """
    lake_width = WIDTH // 6      # tweak size as needed
    lake_height = HEIGHT // 3

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    left = center_x - lake_width // 2
    right = center_x + lake_width // 2
    top = center_y - lake_height // 2
    bottom = center_y + lake_height // 2

    return left <= x <= right and top <= y <= bottom
# -------------------------------------------------------------


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):

                # NEW: water cells never change; copy and skip rules
                if forest[(x, y)] == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue

                # Tree growth on empty spaces (not water)
                if (forest[(x, y)] == EMPTY
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE

                # Lightning strikes trees (not water)
                elif (forest[(x, y)] == TREE
                      and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor_pos = (x + ix, y + iy)
                            neighbor_cell = forest.get(neighbor_pos)

                            # Fire spreads only to neighboring trees,
                            # NOT into water, so WATER remains a firebreak.
                            if neighbor_cell == TREE:
                                nextForest[neighbor_pos] = FIRE

                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object (TREE, EMPTY, etc.).
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure.
    Includes a central lake that is placed once and never modified.
    """
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):

            # NEW: place the lake first so it never gets overwritten
            if is_lake_cell(x, y):
                forest[(x, y)] = WATER  # water cells are permanent
                continue

            # Original tree / empty initialization
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg(WATER_COLOR)
                print(WATER, end='')
            elif cell == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
