import pygame

class ScoreEffect(pygame.sprite.Sprite):
    def __init__(self, points, x, y):
        super().__init__()
        self.font = pygame.font.Font(None, 30)  # Smaller font than main score
        self.points = points
        self.position = pygame.math.Vector2(x, y)
        self.creation_time = pygame.time.get_ticks()
        self.duration = 1000  # Effect lasts 1 second
        self.alpha = 255  # Start fully visible
        
    def update(self, dt):
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.creation_time
        
        if elapsed > self.duration:
            self.kill()
        else:
            # Move upward
            self.position.y -= 100 * dt
            # Fade out
            self.alpha = 255 * (1 - elapsed/self.duration)
    
    def draw(self, screen):
        text = self.font.render(f"+{self.points}", True, (255, 215, 0))
        text.set_alpha(self.alpha)
        screen.blit(text, self.position)