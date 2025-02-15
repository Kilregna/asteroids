import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__ (self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x, y)  # Initialize position as a 2D vector
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Transparent RGBA
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle_coords = self.triangle()
        print("Triangle points:", triangle_coords)
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt