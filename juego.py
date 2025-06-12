import pygame
from player import Player
from bala import Bala
from enemigo import Enemigo
import random

def jugar():
    pygame.init()
    width = 450
    height = 600
    ventana = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Star Blaster")

    nave_img = pygame.image.load("assets/img/nave1.png")
    enemigo_img = pygame.image.load("assets/img/enemigo1.png")

    nave = Player(200, 500, nave_img)
    balas = []
    enemigos = []

    bala_delay = 600
    ultima_bala = pygame.time.get_ticks()
    tiempo_oleada = pygame.time.get_ticks() - 5000
    intervalo_oleada = 4000

    run = True
    while run:
        pygame.time.delay(30)
        ahora = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        nave.movimiento(keys, width)

        if keys[pygame.K_SPACE]:
            if ahora - ultima_bala > bala_delay:
                bala = Bala(nave.rect.centerx - 2, nave.rect.top)
                balas.append(bala)
                ultima_bala = ahora

        if ahora - tiempo_oleada > intervalo_oleada:
            cantidad_enemigos = random.randint(3, 6)
            for i in range(cantidad_enemigos):
                x = random.randint(30, width - 70)
                y = random.randint(-20, 10)
                enemigo = Enemigo(x, y, enemigo_img)
                enemigo.velocidad_x = random.uniform(1.5, 3.5)
                enemigo.velocidad_y = random.uniform(35, 55)
                enemigo.direccion = random.choice([-1, 1])
                enemigos.append(enemigo)
            tiempo_oleada = ahora

        ventana.fill((0, 0, 0))
        nave.draw(ventana)

        for bala in balas[:]:
            bala.movimiento()
            bala.draw(ventana)
            if bala.rect.bottom < 0:
                balas.remove(bala)

        for enemigo in enemigos[:]:
            enemigo.mover(width)
            enemigo.draw(ventana)
            for bala in balas[:]:
                if bala.rect.colliderect(enemigo.rect):
                    enemigos.remove(enemigo)
                    balas.remove(bala)
                    break

        pygame.display.update()

    pygame.quit()