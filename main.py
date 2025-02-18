import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)    
    AsteroidField()
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill(SCREEN_COLOR)
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #Limit the FPS to 60
        dt = fps.tick(60) / 1000
        
if __name__ == "__main__":
    main()