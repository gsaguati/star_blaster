import pygame
from player import Player
pygame.init()

nave = Player(200, 500)

screen_width = 450
screen_height = 600
ventana = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Star Blaster")

run = True
while run:
    pygame.time.delay(30)  
    keys = pygame.key.get_pressed() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    nave.movimiento(keys, screen_width)
    ventana.fill((0, 0, 0))  
    nave.draw(ventana)
    pygame.display.update()

pygame.quit()


