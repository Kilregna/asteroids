import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius    

    def draw(self, screen):
        pygame.draw.circle(screen,0,0,0,2)

    def update(self, dt):
        self.position = self.velocity * dt