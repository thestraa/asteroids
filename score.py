import pygame
from constants import ASTEROID_MIN_RADIUS
from asteroid import Asteroid

class GameScore:
    def __init__(self,):
        # Add this with your other initializations
        self.score = 0
        self.high_score = self.load_high_score() # Load high score when game starts
        self.font = pygame.font.SysFont("simsun", 36)

    def save_high_score(self):
        try:
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        except:
            print("Could not save high score")

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0  # Return 0 if file doesn't exist or has invalid content

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset_score(self):
        self.update_high_score()
        self.score = 0

    def draw(self, screen):
        # Add this to draw the score

        score_text = self.font.render(f"Score: {self.score}", True, "white")
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, "yellow")
        screen.blit(score_text, (10, 10))  # Position in top-left corner
        screen.blit(high_score_text, (10, 40))

    def add_points(self, asteroid_radius):
        if asteroid_radius > ASTEROID_MIN_RADIUS * 2:  # Large asteroid
            self.score += 100
        elif asteroid_radius > ASTEROID_MIN_RADIUS:    # Medium asteroid
            self.score += 50
        else:                                          # Small asteroid
            self.score += 25
        