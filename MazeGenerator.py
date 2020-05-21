import pygame

WIDTH = 440
HEIGHT = 440
FPS = 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze generator")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

grid = []
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


def draw_cell(x, y):
    pygame.draw.rect(screen, BLUE, [x + 1, y + 1, w - 1, w - 1])
    pygame.display.update()


make_grid(20, 0)
draw_cell(80, 20)


running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

