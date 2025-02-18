import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, position, velocity, color, size=2):
        super().__init__()
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(velocity)
        self.color = color
        self.size = size
        self.lifetime = 1.0
        self.birth_time = pygame.time.get_ticks() / 1000.0
        
    def update(self, dt):
        self.position += self.velocity * dt
        current_time = pygame.time.get_ticks() / 1000.0
        if current_time - self.birth_time > self.lifetime:
            self.lifetime = 0
            
    def draw(self, screen):
        current_time = pygame.time.get_ticks() / 1000.0
        age = current_time - self.birth_time
        alpha = 255 * (1 - age/self.lifetime)
        if alpha > 0:
            surf = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, alpha), (self.size, self.size), self.size)
            screen.blit(surf, self.position)