import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tyler's Asteroids Game")

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Score:", True, "white", "black")
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH//16, SCREEN_HEIGHT//16)

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()



    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    

    while pygame.get_init() == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if CircleShape.check_collision(asteroid, player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if CircleShape.check_collision(shot, asteroid):
                    shot.kill()
                    asteroid.split()

        

        screen.fill("black")
        screen.blit(text, textRect)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
    main()