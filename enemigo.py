import pygame

class Enemigo:
    def __init__(self, x, y, imagen):
        self.imagen = imagen
        self.rect = pygame.Rect(x, y, 40, 40)
        self.velocidad_x = 2
        self.velocidad_y = 20
        self.direccion = 1 

    def mover(self, width):
        self.rect.x += self.velocidad_x * self.direccion
        if self.rect.right >= width or self.rect.left <= 0:
            self.direccion *= -1
            self.rect.y += self.velocidad_y

    def draw(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        #pygame.draw.rect(pantalla, (0, 0, 255), self.rect)  
