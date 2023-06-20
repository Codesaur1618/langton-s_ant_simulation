import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up game grid
grid_size = 10
rows = int(screen_height / grid_size)
cols = int(screen_width / grid_size)
grid = np.zeros((rows, cols), dtype=int)

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize ant positions and directions
num_ants = 10
ant_positions = np.zeros((num_ants, 2), dtype=int)
ant_directions = np.zeros(num_ants, dtype=int)

# Set ant positions and directions randomly
for i in range(num_ants):
    ant_positions[i] = np.array([np.random.randint(rows), np.random.randint(cols)])
    ant_directions[i] = np.random.randint(4)

# Run simulation
steps = 30000
for step in range(steps):
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update ant positions and directions
    for i in range(num_ants):
        row, col = ant_positions[i]
        direction = ant_directions[i]

        # Update grid
        if grid[row, col] == 0:
            grid[row, col] = 1
            ant_directions[i] = (direction + 1) % 4
        else:
            grid[row, col] = 0
            ant_directions[i] = (direction - 1) % 4

        # Move ant
        if ant_directions[i] == 0:
            row -= 1
        elif ant_directions[i] == 1:
            col += 1
        elif ant_directions[i] == 2:
            row += 1
        else:
            col -= 1

        # Wrap ant around edges of screen
        row = row % rows
        col = col % cols

        ant_positions[i] = np.array([row, col])

    # Draw grid and ants
    screen.fill(black)
    for row in range(rows):
        for col in range(cols):
            x = col * grid_size
            y = row * grid_size
            if grid[row, col] == 1:
                pygame.draw.rect(screen, white, (x, y, grid_size, grid_size))
    for i in range(num_ants):
        x = ant_positions[i, 1] * grid_size
        y = ant_positions[i, 0] * grid_size
        if ant_directions[i] == 0:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, grid_size, grid_size))
        elif ant_directions[i] == 1:
            pygame.draw.rect(screen, (0, 255, 0), (x, y, grid_size, grid_size))
        elif ant_directions[i] == 2:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, grid_size, grid_size))
        else:
            pygame.draw.rect(screen, (255, 255, 0), (x, y, grid_size, grid_size))

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
