import numpy as np
import random

# creates a grid of zeros with the specified width and height 
def dead_state(width, hight):
    grid = np.zeros((hight, width))
    return grid

# creates a grid with random values of 0 and 1
def random_state(width, hight):
    state = dead_state(width, hight)
    for r in range(hight):
        for c in range(width):
            random_number = random.random()
            if random_number < 0.5:
                state[r, c] = 0
            else:
                state[r, c] = 1
    return state

# renders the state of the grid( dead = "." , alive = "O")
def render(state):
    for row in state:
        for cell in row:
            if cell == 1:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Test
render(random_state(30, 20))