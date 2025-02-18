import pygame
import random
import math
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    # Create random points around the circle
        self.points = []
        num_points = 8  # number of vertices
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            # Vary the radius slightly for each point
            offset = random.uniform(0.8, 1.2)
            point_radius = self.radius * offset
            point_x = math.cos(angle) * point_radius
            point_y = math.sin(angle) * point_radius
            self.points.append((point_x, point_y))

    def draw(self, screen):
        screen_points = [(self.position.x + px, self.position.y + py) for px, py in self.points]
        pygame.draw.polygon(screen, "gray", screen_points, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius =  self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_velocity1 * 1.2
        asteroid_2.velocity = new_velocity2 * 1.2