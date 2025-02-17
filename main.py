import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        screen.fill(SCREEN_COLOR)
        player.draw(screen)
        pygame.display.flip()

        #Limit the FPS to 60
        dt = fps.tick(60) / 1000
if __name__ == "__main__":
    main()