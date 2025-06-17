import pygame

class Enemigo2:
    def __init__(self, x, y, imagen):
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = 2
        self.direccion = 1 

        self.ultimo_disparo = pygame.time.get_ticks()
        self.frecuencia_disparo = 1500 

    def mover(self, width):
        self.rect.y += self.velocidad
        self.rect.x += self.direccion * 2
        if self.rect.left <= 0 or self.rect.right >= width:
            self.direccion *= -1

    def draw(self, ventana):
        ventana.blit(self.image, self.rect)
