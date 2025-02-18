import pygame
import sys
from gameover import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import GameScore

def initialize_game():
    """Resets all game objects and variables."""
    global updatable, drawable, asteroids, player, asteroid_field, shots, score_display
    
    # Reset sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # Redefine containers for the Player and Asteroids
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create new player and asteroids
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score_display = GameScore() # Calling score and highscore to display
    score_display.reset_score()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    
    # Initialize game state for the first time
    initialize_game()
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collision(asteroid):
                score_display.update_high_score() #Updates high_score
                game_over_loop(screen)  # Call Game Over loop
                initialize_game()       # Reinitialize the game objects

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    score_display.add_points(asteroid.radius) # Increasing score when asteroid gets destroyed
                    asteroid.split()

                

        screen.fill(SCREEN_COLOR)
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        score_display.draw(screen)

        pygame.display.flip()

        #Limit the FPS to 60
        dt = fps.tick(60) / 1000
        
if __name__ == "__main__":
    main()