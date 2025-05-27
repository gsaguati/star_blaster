import pygame
from player import Player
from bala import Bala

pygame.init()
nave_img = pygame.image.load("assets/img/nave1.png")
nave = Player(200, 500, nave_img)

width = 450
height = 600
ventana = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Blaster")

balas = []
bala_delay = 300  
ultima_bala = pygame.time.get_ticks()  

run = True
while run:
    pygame.time.delay(30)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    nave.movimiento(keys, width)

    ahora = pygame.time.get_ticks()
    if keys[pygame.K_SPACE]:
        if ahora - ultima_bala > bala_delay:
            bala = Bala(nave.rect.centerx - 2, nave.rect.top)
            balas.append(bala)
            ultima_bala = ahora

    ventana.fill((0, 0, 0))
    nave.draw(ventana)

    for bala in balas[:]:
        bala.movimiento()
        bala.draw(ventana)
        if bala.rect.bottom < 0:
            balas.remove(bala)

    pygame.display.update()

pygame.quit()
