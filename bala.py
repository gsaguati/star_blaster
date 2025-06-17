import pygame

class Bala:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.speed = 12

    def movimiento(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
