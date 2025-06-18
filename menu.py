import pygame 
import sys
import juego
import os
import nombre
import score

def menu_principal():
    pygame.init()
    ventana = pygame.display.set_mode((450, 600))
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

    fuente = pygame.font.Font("assets/font/KarmaticArcade-6Yrp1.ttf", 36)
    texto = fuente.render("Star Blaster", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(225, 100))

    boton_rect = pygame.Rect(150, 225, 150, 50)
    texto_boton = fuente.render("JUGAR", True, (255, 255, 255))  
    texto_rect1 = texto_boton.get_rect(center=boton_rect.center)

    boton_rect2 = pygame.Rect(150, 325, 150, 50)
    texto_boton2 = fuente.render("SCORE", True, (255, 255, 255))
    texto_rect2 = texto_boton2.get_rect(center=boton_rect2.center)  

    boton_rect4 = pygame.Rect(150, 425, 150, 50)
    texto_boton3 = fuente.render("SALIR", True, (255, 255, 255))
    texto_rect3 = texto_boton3.get_rect(center=boton_rect4.center)

    score.crear_base_datos()

    run = True
    while run:
        mouse = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

        ventana.blit(frames_fondo[indice_frame], (0, 0))
        indice_frame = (indice_frame + 1) % len(frames_fondo)

        ventana.blit(texto, texto_rect)     
        ventana.blit(texto_boton, texto_rect1)
        ventana.blit(texto_boton2, texto_rect2)
        ventana.blit(texto_boton3, texto_rect3)

        if boton_rect.collidepoint(mouse) and clic[0]:
            nombre_jugador = nombre.ingresar_nombre()
            if nombre_jugador:
                puntaje = juego.jugar(nombre_jugador)
                score.guardar_puntaje(nombre_jugador, puntaje)
                sys.exit()

        if boton_rect2.collidepoint(mouse) and clic[0]:
          pygame.quit()
          score.mostrar_pantalla_scores()
          sys.exit()


        if boton_rect4.collidepoint(mouse) and clic[0]:
            pygame.quit()
            sys.exit()

        pygame.display.flip()
        reloj.tick(fps_animacion) 

    pygame.quit()
if __name__ == "__main__":
    menu_principal()
