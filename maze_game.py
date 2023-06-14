import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the dimensions of the maze
maze_width = 600
maze_height = 600
cell_size = 30

# Define the maze as a 2D array
maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9],
    [9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 0, 9, 9, 9, 9, 9, 9, 9, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 0, 9, 0, 9, 9, 0, 9, 9, 0, 9, 9, 9, 0, 9],
    [9, 0, 9, 0, 0, 9, 0, 9, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 0, 9, 0, 9, 0, 9],
    [9, 0, 0, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 9],
    [9, 9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 0, 9, 0, 0, 0, 0, 0, 2, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9],
    [9, 9, 9, 9, 9, 9, 9, 0, 9, 0, 9, 9, 9, 9, 9],
    [9, 0, 9, 9, 9, 9, 9, 0, 9, 0, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

# Define the agent's position
agent_x = 1
agent_y = 1

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((maze_width, maze_height))
pygame.display.set_caption("Maze Game")

# Set up clock for frame rate
clock = pygame.time.Clock()

# Function to draw the maze
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:  # Start cell
                pygame.draw.rect(screen, GREEN, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif maze[y][x] == 2:  # Finish cell
                pygame.draw.rect(screen, RED, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif maze[y][x] == 9:  # Walls
                pygame.draw.rect(screen, BLACK, (x * cell_size, y * cell_size, cell_size, cell_size))
            else:  # Paths
                pygame.draw.rect(screen, WHITE, (x * cell_size, y * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size), 1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Move the agent based on arrow key input
            if event.key == pygame.K_UP and maze[agent_y - 1][agent_x] != 9:
                agent_y -= 1
            elif event.key == pygame.K_DOWN and maze[agent_y + 1][agent_x] != 9:
                agent_y += 1
            elif event.key == pygame.K_LEFT and maze[agent_y][agent_x - 1] != 9:
                agent_x -= 1
            elif event.key == pygame.K_RIGHT and maze[agent_y][agent_x + 1] != 9:
                agent_x += 1

    # Clear the screen
    screen.fill(BLACK)

    # Draw the maze
    draw_maze()

    # Draw the agent
    pygame.draw.circle(screen, BLUE, (agent_x * cell_size + cell_size // 2, agent_y * cell_size + cell_size // 2),
                       cell_size // 4)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
