import pygame
import numpy as np
#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#window
WINDOW_SIZE = (800, 600)
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Langton's Ant")
#grid and the ant
GRID_SIZE = (100, 100)
grid = np.zeros(GRID_SIZE, dtype=np.uint8)
ant_pos = (GRID_SIZE[0] // 2, GRID_SIZE[1] // 2)
ant_dir = 0  # 0=up, 1=right, 2=down, 3=left
#clock time quantum
clock = pygame.time.Clock()
fps = 60
#the main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    # Update the ant and the grid
    if grid[ant_pos] == 0:
        ant_dir = (ant_dir - 1) % 4
        grid[ant_pos] = 1
    else:
        ant_dir = (ant_dir + 1) % 4
        grid[ant_pos] = 0

    if ant_dir == 0:
        ant_pos = (ant_pos[0], ant_pos[1] - 1)
    elif ant_dir == 1:
        ant_pos = (ant_pos[0] + 1, ant_pos[1])
    elif ant_dir == 2:
        ant_pos = (ant_pos[0], ant_pos[1] + 1)
    elif ant_dir == 3:
        ant_pos = (ant_pos[0] - 1, ant_pos[1])
    screen.fill(BLACK)
    # Draw the grid
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i * 5, j * 5, 5, 5))
    # Draw the ant
    pygame.draw.rect(screen, WHITE, (ant_pos[0] * 5, ant_pos[1] * 5, 5, 5))
    pygame.display.flip()
    clock.tick(fps)
