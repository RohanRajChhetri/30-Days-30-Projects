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

def next_board_state(height,width,state):
    new_state = np.copy(state)

    for x in range(height):
        for y in range(width):
            # Count the number of alive neighbors
            alive_neighbors = 0

            # loop through the neighbors
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    ni = x + i
                    nj = y + j
                    if (0 <= ni < height) and (0 <= nj < width):
                        alive_neighbors += state[ni][nj]

            #rules of the Game of Life
            if state[x][y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    state[x][y] = 0
            else:
                if alive_neighbors == 3:
                    state[x][y] = 1

    return new_state

# Test
if __name__ == "__main__":
    width = 10
    height = 10
    state = random_state(width, height)
    render(state)

    # Run for 5 iterations
    for _ in range(5):  
        next_board_state(height, width, state)
        render(state)