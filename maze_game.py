import pygame
import os

WIDTH = 600
HEIGHT = 600
FPS = 30

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

os.environ['SDL_VIDEO_CENTERED'] = '1'  #  center whole window position

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze game")
clock = pygame.time.Clock()

CELL_SIZE = 24

levels = []

level_1 = [
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'XP XXXXXXX          XXXXX',
    'X  XXXXXXX  XXXXXX  XXXXX',
    'X       XX  XXXXXX  XXXXX',
    'X       XX  XXX        XX',
    'XXXXXX  XX  XXX        XX',
    'XXXXXX  XX  XXXXXX  XXXXX',
    'XXXXXX  XX    XXXX  XXXXX',
    'X  XXX        XXXX  XXXXX',
    'X  XXX  XXXXXXXXXXXXXXXXX',
    'X         XXXXXXXXXXXXXXX',
    'X                XXXXXXXX',
    'XXXXXXXXXXXX     XXXXX  X',
    'XXXXXXXXXXXXXXX  XXXXX  X',
    'XXX  XXXXXXXXXX         X',
    'XXX                     X',
    'XXX         XXXXXXXXXXXXX',
    'XXXXXXXXXX  XXXXXXXXXXXXX',
    'XXXXXXXXXX              X',
    'XX   XXXXX              X',
    'XX   XXXXXXXXXXXXX  XXXXX',
    'XX    YXXXXXXXXXXX  XXXXX',
    'XX          XXXX        X',
    'XXXX                    X',
    'XXXXXXXXXXXXXXXXXXXXXXXXX',
]

levels.append(level_1)


def mark_cell(x, y, color):
    pygame.draw.rect(screen, color, [x + 1, y + 1, CELL_SIZE - 1, CELL_SIZE - 1])


def setup_up_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            x_coor = x * CELL_SIZE
            y_coor = y * CELL_SIZE
            if character == "X":
                mark_cell(x_coor, y_coor, (255, 255, 255))


running = True
while running:
    screen.blit(BG, (0,0))
    setup_up_maze(levels[0])
    pygame.display.update()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()