import pygame

class BalaEnemiga:
    def __init__(self, x, y, velocidad=5):
        self.imagen = pygame.image.load("assets/img/bala_enemigo.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (5, 13))
        self.rect = pygame.Rect(x, y, 5, 13)
        self.velocidad = velocidad

    def movimiento(self):
        self.rect.y += self.velocidad

    def draw(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
