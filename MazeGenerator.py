import pygame
import random
import time
from collections import deque

WIDTH = 440
HEIGHT = 440
FPS = 30
DELAY = 0.01

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

grid = []
stack = deque()
visited = []
solution = {}
w = 20


def make_grid(x, y):
    init_x = x
    for i in range(1, 21):
        x = init_x
        y += 20
        for j in range(1, 21):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])  # up
            pygame.draw.line(screen, WHITE, [x, y], [x, y + w])  # left
            pygame.draw.line(screen, WHITE, [x, y + w], [x + w, y + w])  # down
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])  # right
            grid.append((x, y))
            x = x + 20
    pygame.display.update()


def mark_solution_cell(x, y, color):
    pygame.draw.rect(screen, color, [x + 9, y + 9, w - 18, w - 18])
    pygame.display.update()


def mark_cell(x, y, color):
    pygame.draw.rect(screen, color, [x + 1, y + 1, w - 1, w - 1])
    pygame.display.update()


def go_up(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y - w + 1, w - 1, 2*w - 1])
    pygame.display.update()


def go_down(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y + 1, w - 1, 2*w - 1])
    pygame.display.update()


def go_right(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y + 1, 2*w - 1, w - 1])
    pygame.display.update()


def go_left(x, y):
    pygame.draw.rect(screen, BLUE, [x - w + 1, y + 1, 2*w - 1, w - 1])
    pygame.display.update()


def get_unvisited_neighbors(x, y):
    neighbors = []
    if (x + w, y) in grid and (x + w, y) not in visited:  # right neighbor
        neighbors.append((x + w, y))
    if ((x, y + w)) in grid and (x, y + w) not in visited:  # down neighbor
        neighbors.append((x, y + w))
    if (x - w, y) in grid and (x - w, y) not in visited:  # left neighbor
        neighbors.append((x - w, y))
    if (x, y - w) in grid and (x, y - w) not in visited:  # up neighbor
        neighbors.append((x, y - w))
    return neighbors
    

def generate_maze(x, y):
    # Choose the initial cell, mark it as visited and push it to the stack
    mark_cell(x, y, BLUE)
    visited.append((x, y))
    stack.append((x, y))
    # While the stack is not empty
    while len(stack) > 0:
        # pop a cell from the stack and make it a current cell
        (current_cell_x, current_cell_y)  = stack.pop()

        # If the current cell has any neighbours which have not been visited 
        neighbors = get_unvisited_neighbors(current_cell_x, current_cell_y)
        if len(neighbors) > 0:
            # Push the current cell to the stack
            stack.append((current_cell_x, current_cell_y))

            # Choose one of the unvisited neighbours
            next_neighbor_index = random.randint(0, len(neighbors) - 1)
            (next_cell_x, next_cell_y) = neighbors[next_neighbor_index]
            
            # Remove the wall between the current cell and the chosen cell
            if current_cell_x == next_cell_x and next_cell_y == current_cell_y + w:
                go_down(current_cell_x, current_cell_y)
            if current_cell_x == next_cell_x and next_cell_y == current_cell_y - w:
                go_up(current_cell_x, current_cell_y)
            if current_cell_y == next_cell_y and next_cell_x == current_cell_x + w:
                go_right(current_cell_x, current_cell_y)
            if current_cell_y == next_cell_y and next_cell_x == current_cell_x - w:
                go_left(current_cell_x, current_cell_y)

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


make_grid(20, 0)
generate_maze(20, 20)
show_solution(400, 400)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

