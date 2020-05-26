import pygame
import os
import random

WIDTH = 800
HEIGHT = 700
FPS = 30
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
PLAYER = pygame.image.load(os.path.join("assets", "spaceShips_006.png"))
SHIP_RED = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
SHIP_BLUE = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
SHIP_GREEN = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
LASER_YELLOW = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
LASER_RED = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
LASER_GREEN = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
LASER_BLUE = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center whole window position
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
CLOCK = pygame.time.Clock()


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.cool_down_counter = 0
        self.lasers = []

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def cool_down(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser("yellow", self.x - 20, self.y)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def move_lasers(self, speed):
        self.cool_down()
        for laser in self.lasers:
            laser.y -= speed


class Laser(Ship):
    colors = {
        "red": LASER_RED,
        "blue": LASER_BLUE,
        "green": LASER_GREEN,
        "yellow": LASER_YELLOW
    }

    def __init__(self, color, x, y):
        super().__init__(x, y)
        self.image = self.colors[color]
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        super().draw()


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
    enemy_speed = 4
    enemies = []
    wave = 0

    def redraw_window():
        WIN.blit(BG, (0, 0))
        player.draw()
        for l in player.lasers:
            l.draw()

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
                                     random.randrange(-1500, -50)))

        for e in enemies:
            e.move(enemy_speed)

            if e.y + e.get_height() > HEIGHT:
                enemies.remove(e)

        player.move_lasers(5)

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
        if keys[pygame.K_SPACE]:
            player.shoot()

    pygame.quit()


if __name__ == '__main__':
    main()
