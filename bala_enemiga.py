import pygame

class BalaEnemiga:
    def __init__(self, x, y, velocidad=5):
        self.rect = pygame.Rect(x, y, 4, 10)
        self.velocidad = velocidad

    def movimiento(self):
        self.rect.y += self.velocidad

    def draw(self, pantalla):
        pygame.draw.rect(pantalla, (255, 0, 0), self.rect)  
