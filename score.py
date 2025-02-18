import pygame
from constants import ASTEROID_MIN_RADIUS
from  scoreeffects import ScoreEffect

class GameScore:
    def __init__(self,):
        # Add this with your other initializations
        self.score = 0
        self.high_score = self.load_high_score() # Load high score when game starts
        self.font = pygame.font.SysFont("simsun", 36)
        self.score_effects = [] 
        self.is_new_high_score = False

    def is_high_score(self):
        return self.score > self.high_score
       
    def draw(self, screen):
        # Add this to draw the score
        score_text = self.font.render(f"Score: {self.score}", True, "white")
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, "yellow")
        screen.blit(score_text, (10, 10))  # Position in top-left corner
        screen.blit(high_score_text, (10, 40))

              # Update and draw score effects
        for effect in self.score_effects[:]:  # Create a copy of the list to iterate
            effect.update(1/60)  # Assuming 60 FPS
            effect.draw(screen)
            if effect.alpha <= 0:  # Remove completed effects
                self.score_effects.remove(effect)

    def add_points(self, asteroid_radius, x, y):  # Added x, y parameters
        # Calculate points based on size
        if asteroid_radius > ASTEROID_MIN_RADIUS * 2:
            points = 100
        elif asteroid_radius > ASTEROID_MIN_RADIUS:
            points = 50
        else:
            points = 25

        self.score += points
        # Create new score effect at asteroid's position
        self.score_effects.append(ScoreEffect(points, x, y))
        
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
        
    def check_high_score(self):
        # New method to check if current score is a high score
        if self.score > self.high_score:
            self.is_new_high_score = True
            return True
        return False
    
    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
            self.is_new_high_score = True  # Set the flag
            return True
        return False
    
    def reset_score(self):
        self.score = 0
        self.is_new_high_score = False
        self.score_effects.clear()  # Clear any remaining score effects