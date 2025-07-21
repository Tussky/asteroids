import pygame

from asteroidfield import AsteroidField
from asteroids import Asteroid
from constants import (ASTEROID_KINDS, ASTEROID_MAX_RADIUS,
                       ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE, SCREEN_HEIGHT,
                       SCREEN_WIDTH)
from player import Player
from shot import Shot


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", 720)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroid_group)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers =  all_shots 

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        screen.fill((0, 0, 0))
        for to_draw in drawable:  # for some reason this must be individual
            to_draw.draw(screen)
        for shot in all_shots:
            shot.update(dt)
            shot.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1_000

        updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collides_with(player):
                return
        for shot in all_shots:
            for asteroid in asteroid_group:
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()  # renders the screen


if __name__ == "__main__":
    main()
