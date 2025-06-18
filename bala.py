import pygame

class Bala:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("assets/img/bala.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (5, 13))
        self.rect = pygame.Rect(x, y, 5, 13)
        self.speed = 12

    def movimiento(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.imagen, self.rect)
