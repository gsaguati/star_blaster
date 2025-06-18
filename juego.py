import pygame
import os
from player import Player
from bala import Bala
from enemigo import Enemigo
from enemigo2 import Enemigo2
from bala_enemiga import BalaEnemiga
import random
import game_over
import score 


def jugar(nombre):
    pygame.init()
    width = 450
    height = 600
    ventana = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Star Blaster")
    pygame.mixer.music.load("assets/sonidos/base2.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    frames_fondo = []
    fondo = "assets/img/split"
    archivos = sorted(os.listdir(fondo))
    for archivo in archivos:
        if archivo.endswith(".jpg") and "frame" in archivo:
            ruta = os.path.join(fondo, archivo)
            imagen = pygame.image.load(ruta).convert()
            imagen = pygame.transform.scale(imagen, (450, 600))
            frames_fondo.append(imagen)

    indice_frame = 0
    fps_animacion = 25
    reloj = pygame.time.Clock()

    nave_img = pygame.image.load("assets/img/nave2.png")
    enemigo_img = pygame.image.load("assets/img/enemigo.png")
    enemigo2_img = pygame.image.load("assets/img/enemigo_2.png") 
    nave_mini = pygame.transform.scale(nave_img, (25, 25))
    sonido_disparo = pygame.mixer.Sound("assets/sonidos/bala.wav")
    sonido_disparo.set_volume(0.5)
    sonido_enemigo = pygame.mixer.Sound("assets/sonidos/enemigo.wav")
    sonido_enemigo.set_volume(0.5)
    sonido_enemigo2 = pygame.mixer.Sound("assets/sonidos/enemigo2.wav")
    sonido_enemigo2.set_volume(0.5)
    


    nave = Player(200, 500, nave_img)
    balas = []
    balas_enemigas = []
    enemigos = []
    enemigos2 = []

    bala_delay = 600
    ultima_bala = pygame.time.get_ticks()
    tiempo_oleada = pygame.time.get_ticks() - 4500
    tiempo_enemigos2 = pygame.time.get_ticks() - 4000
    intervalo_oleada = 4000
    intervalo_enemigos2 = 2500  

    fuente = pygame.font.SysFont(None, 36)
    puntaje = 0
    run = True
    while run:
        pygame.time.delay(30)
        ahora = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ventana.blit(frames_fondo[indice_frame], (0, 0))
        indice_frame = (indice_frame + 1) % len(frames_fondo)
        nave.movimiento(keys, width)

        if keys[pygame.K_SPACE]:
            if ahora - ultima_bala > bala_delay:
                bala = Bala(nave.rect.centerx - 2, nave.rect.top)
                balas.append(bala)
                sonido_disparo.play()
                ultima_bala = ahora

        # Enemigo 1
        if ahora - tiempo_oleada > intervalo_oleada:
            cantidad_enemigos = random.randint(3, 6)
            for i in range(cantidad_enemigos):
                x = random.randint(30, width - 70)
                y = random.randint(-20, 10)
                enemigo = Enemigo(x, y, enemigo_img)
                enemigo.velocidad_x = random.uniform(3.5, 5.5)
                enemigo.velocidad_y = random.uniform(65, 85)
                enemigo.direccion = random.choice([-1, 1])
                enemigos.append(enemigo)
            tiempo_oleada = ahora

        # Enemigo 2
        if ahora - tiempo_enemigos2 > intervalo_enemigos2:
            cantidad = random.randint(0, 1)
            for _ in range(cantidad):
                x = random.randint(30, width - 70)
                y = random.randint(-20, 10)
                enemigo = Enemigo2(x, y, enemigo2_img)
                enemigos2.append(enemigo)
            tiempo_enemigos2 = ahora

        nave.draw(ventana)

        vidas_y = height - nave_mini.get_height() - 10
        for i in range(nave.vidas):
            x = 10 + i * 30
            ventana.blit(nave_mini, (x, vidas_y))

        for bala in balas[:]:
            bala.movimiento()
            bala.draw(ventana)
            if bala.rect.bottom < 0:
                balas.remove(bala)

        for enemigo in enemigos[:]:
            enemigo.mover(width)
            enemigo.draw(ventana)
            if enemigo.rect.colliderect(nave.rect) or enemigo.rect.top > nave.rect.bottom:
                enemigos.remove(enemigo)
                nave.vidas -= 1
                if nave.vidas <= 0:
                    run = False
                continue

            for bala in balas[:]:
                if bala.rect.colliderect(enemigo.rect):
                    enemigos.remove(enemigo)
                    balas.remove(bala)
                    sonido_enemigo.play()
                    puntaje += 100
                    break

        for enemigo in enemigos2[:]:
            enemigo.mover(width)
            enemigo.draw(ventana)
            if enemigo.rect.colliderect(nave.rect) or enemigo.rect.top > nave.rect.bottom:
                enemigos2.remove(enemigo)
                nave.vidas -= 1
                if nave.vidas <= 0:
                    run = False
                continue

            if ahora - enemigo.ultimo_disparo > enemigo.frecuencia_disparo:
                bala_enemiga = BalaEnemiga(enemigo.rect.centerx, enemigo.rect.bottom)
                balas_enemigas.append(bala_enemiga)
                enemigo.ultimo_disparo = ahora

            for bala in balas[:]:
                if bala.rect.colliderect(enemigo.rect):
                    enemigos2.remove(enemigo)
                    balas.remove(bala)
                    sonido_enemigo2.play()
                    puntaje += 250
                    break

        for bala in balas_enemigas[:]:
            bala.movimiento()
            bala.draw(ventana)
            if bala.rect.top > height:
                balas_enemigas.remove(bala)
            elif bala.rect.colliderect(nave.rect):
                balas_enemigas.remove(bala)
                nave.vidas -= 1
                if nave.vidas <= 0:
                    run = False

        texto_puntaje = fuente.render(f"Score: {puntaje}", True, (255, 255, 255))
        ventana.blit(texto_puntaje, (width - texto_puntaje.get_width() - 10, height - texto_puntaje.get_height() - 10))

        pygame.display.update()
        reloj.tick(fps_animacion)

    if nave.vidas <= 0:
        score.guardar_puntaje(nombre, puntaje)
        game_over.game_over(nombre)

    return puntaje
