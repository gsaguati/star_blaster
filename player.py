import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.speed = 6

    def movimiento(self, keys, screen_width):
     if keys[pygame.K_LEFT]:
        if self.rect.left > 0:
            self.rect.x -= self.speed
     elif keys[pygame.K_RIGHT]:
        if self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
