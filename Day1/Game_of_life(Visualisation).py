import pygame
import random
import numpy as np

# Game settings
width, height = 800, 600  # screen size
cell_size = 10            # size of each cell (adjustable)

# Calculate grid dimensions
cols = width // cell_size
rows = height // cell_size

# Colors
ALIVE_COLOR = (0, 255, 0)  # Green for alive cells
DEAD_COLOR = (0, 0, 0)     # Black for dead cells

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

# Game state
def dead_state():
    return np.zeros((rows, cols))

def random_state():
    return np.random.choice([0, 1], size=(rows, cols))

# Rendering the state
def render(state):
    for row in range(rows):
        for col in range(cols):
            color = ALIVE_COLOR if state[row, col] == 1 else DEAD_COLOR
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Computing next generation (Game of Life rules)
def next_board_state(state):
    new_state = np.copy(state)
    for x in range(rows):
        for y in range(cols):
            alive_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    ni, nj = x + i, y + j
                    if 0 <= ni < rows and 0 <= nj < cols:
                        alive_neighbors += state[ni, nj]

            if state[x, y] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_state[x, y] = 0
            else:
                if alive_neighbors == 3:
                    new_state[x, y] = 1

    return new_state

# Main loop
def game_of_life():
    state = random_state()  # initial random state

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(DEAD_COLOR)  # clear screen (set all cells to dead)
        render(state)            # render current state
        
        # Handle events (e.g., user closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        state = next_board_state(state)  # get next state
        pygame.display.update()  # update screen
        clock.tick(10)  # control the frame rate (10 frames per second)

    pygame.quit()

# Start the simulation
if __name__ == "__main__":
    game_of_life()
