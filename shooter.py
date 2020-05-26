import pygame
import os
import random

WIDTH = 800
HEIGHT = 700
FPS = 30
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
PLAYER = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
SHIP_RED = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
SHIP_BLUE = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
SHIP_GREEN = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center whole window position
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
CLOCK = pygame.time.Clock()


class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()


class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = PLAYER
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        super().draw()


class Enemy(Ship):
    colors = {
        "red": SHIP_RED,
        "blue": SHIP_BLUE,
        "green": SHIP_GREEN
    }

    def __init__(self, color, x, y):
        super().__init__(x, y)
        self.image = self.colors[color]
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        super().draw()

    def move(self, speed):
        self.y += speed


def main():
    player = Player(WIDTH // 2, HEIGHT - 100)
    player_speed = 10
    enemy_speed = 1
    enemies = []
    wave = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))
        player.draw()
        for e in enemies:
            e.draw()

        pygame.display.update()

    running = True
    while running:
        redraw_window()

        CLOCK.tick(FPS)

        if len(enemies) == 0:
            wave += 5
            for i in range(wave):
                enemies.append(Enemy(random.choice(["red", "green", "blue"]),
                                     random.randrange(0, WIDTH - 100),
                                     random.randrange(-1500, -100)))

        for e in enemies:
            e.move(enemy_speed + random.randrange(0, 5))

            if e.y + e.get_height() > HEIGHT:
                enemies.remove(e)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player.get_width() < WIDTH:
            player.x += player_speed
        if keys[pygame.K_w] and player.y > 0:
            player.y -= player_speed
        if keys[pygame.K_s] and player.y + player.get_height() < HEIGHT:
            player.y += player_speed

    pygame.quit()


if __name__ == '__main__':
    main()
