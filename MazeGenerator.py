import pygame
import random
import time
from collections import deque

WIDTH = 640
HEIGHT = 640
FPS = 30
DELAY = 0.02

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

CELL_SIZE = 20
ROWS = 30
COLS = 30

grid = []
stack = deque()
visited = []
solution = {}


def make_grid(x, y):
    init_x = x
    for i in range(0, ROWS):
        x = init_x
        y += CELL_SIZE
        for j in range(0, COLS):
            pygame.draw.line(screen, WHITE, [x, y], [x + CELL_SIZE, y])  # up
            pygame.draw.line(screen, WHITE, [x, y], [x, y + CELL_SIZE])  # left
            pygame.draw.line(screen, WHITE, [x, y + CELL_SIZE], [x + CELL_SIZE, y + CELL_SIZE])  # down
            pygame.draw.line(screen, WHITE, [x + CELL_SIZE, y], [x + CELL_SIZE, y + CELL_SIZE])  # right
            grid.append((x, y))
            x = x + CELL_SIZE
    pygame.display.update()


def mark_solution_cell(x, y, color):
    pygame.draw.rect(screen, color, [x + int(CELL_SIZE / 2), y + int(CELL_SIZE / 2), 2, 2])
    pygame.display.update()


def mark_cell(x, y, color):
    pygame.draw.rect(screen, color, [x + 1, y + 1, CELL_SIZE - 1, CELL_SIZE - 1])
    pygame.display.update()


def go_up(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y - CELL_SIZE + 1, CELL_SIZE - 1, 2 * CELL_SIZE - 1])
    pygame.display.update()


def go_down(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y + 1, CELL_SIZE - 1, 2 * CELL_SIZE - 1])
    pygame.display.update()


def go_right(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y + 1, 2 * CELL_SIZE - 1, CELL_SIZE - 1])
    pygame.display.update()


def go_left(x, y):
    pygame.draw.rect(screen, BLUE, [x - CELL_SIZE + 1, y + 1, 2 * CELL_SIZE - 1, CELL_SIZE - 1])
    pygame.display.update()


def get_unvisited_neighbors(x, y):
    neighbors = []
    if (x + CELL_SIZE, y) in grid and (x + CELL_SIZE, y) not in visited:  # right neighbor
        neighbors.append((x + CELL_SIZE, y))
    if (x, y + CELL_SIZE) in grid and (x, y + CELL_SIZE) not in visited:  # down neighbor
        neighbors.append((x, y + CELL_SIZE))
    if (x - CELL_SIZE, y) in grid and (x - CELL_SIZE, y) not in visited:  # left neighbor
        neighbors.append((x - CELL_SIZE, y))
    if (x, y - CELL_SIZE) in grid and (x, y - CELL_SIZE) not in visited:  # up neighbor
        neighbors.append((x, y - CELL_SIZE))
    return neighbors


def remove_walls_between_cells(x1, y1, x2, y2):
    if x1 == x2 and y2 == y1 + CELL_SIZE:
        go_down(x1, y1)
    if x1 == x2 and y2 == y1 - CELL_SIZE:
        go_up(x1, y1)
    if y1 == y2 and x2 == x1 + CELL_SIZE:
        go_right(x1, y1)
    if y1 == y2 and x2 == x1 - CELL_SIZE:
        go_left(x1, y1)


def generate_maze(x, y):
    # Choose the initial cell, mark it as visited and push it to the stack
    mark_cell(x, y, BLUE)
    visited.append((x, y))
    stack.append((x, y))
    # While the stack is not empty
    while len(stack) > 0:
        # pop a cell from the stack and make it a current cell
        (current_cell_x, current_cell_y) = stack.pop()

        # If the current cell has any neighbours which have not been visited 
        neighbors = get_unvisited_neighbors(current_cell_x, current_cell_y)
        if len(neighbors) > 0:
            # Push the current cell to the stack
            stack.append((current_cell_x, current_cell_y))

            # Choose one of the unvisited neighbours
            next_neighbor_index = random.randint(0, len(neighbors) - 1)
            (next_cell_x, next_cell_y) = neighbors[next_neighbor_index]

            # Remove the wall between the current cell and the chosen cell
            remove_walls_between_cells(current_cell_x, current_cell_y, next_cell_x, next_cell_y)

            # Mark the chosen cell as visited and push it to the stack
            visited.append((next_cell_x, next_cell_y))
            stack.append((next_cell_x, next_cell_y))
            solution[(next_cell_x, next_cell_y)] = (current_cell_x, current_cell_y)

            time.sleep(DELAY)
        else:
            # just show backtracking cell
            mark_cell(current_cell_x, current_cell_y, GREEN)
            time.sleep(DELAY)
            mark_cell(current_cell_x, current_cell_y, BLUE)
            time.sleep(DELAY)


def show_solution(x, y):
    mark_solution_cell(x, y, WHITE)
    while (x, y) != (20, 20):
        x, y = solution[(x, y)]
        mark_solution_cell(x, y, WHITE)
        time.sleep(DELAY)


make_grid(CELL_SIZE, 0)
generate_maze(CELL_SIZE, CELL_SIZE)
show_solution(ROWS * CELL_SIZE, COLS * CELL_SIZE)  # solution starting from the last cell (bottom right corner)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
