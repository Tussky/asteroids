import pygame

from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", 720)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:

        screen.fill((0, 0, 0))
        player.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1_000

        player.update(dt)

        pygame.display.flip()  # renders the screen


if __name__ == "__main__":
    main()
