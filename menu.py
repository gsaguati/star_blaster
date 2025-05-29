import pygame
import sys
import juego 

pygame.init()
pantalla = pygame.display.set_mode((450, 600))
pygame.display.set_caption("Star Blaster")

fuente = pygame.font.Font("assets/font/KarmaticArcade-6Yrp1.ttf", 36)
texto = fuente.render("Star Blaster", True, (255, 255, 255))
texto_rect = texto.get_rect(center=(225, 100))
boton_rect = pygame.Rect(150, 225, 150, 50)
texto_boton = fuente.render("JUGAR", True, (255, 255, 255))  
texto_rect1 = texto_boton.get_rect(center=boton_rect.center)

boton_rect2 = pygame.Rect(150, 325, 150, 50)
texto_boton2 = fuente.render("SCORE", True, (255, 255, 255))
texto_rect3 = texto_boton.get_rect(center=boton_rect2.center)  

boton_rect4 = pygame.Rect(157, 425, 150, 50)
texto_boton3 = fuente.render("SALIR", True, (255, 255, 255))
texto_rect3 = texto_boton.get_rect(center=boton_rect4.center)


run = True
while run:
    mouse = pygame.mouse.get_pos()
    clic = pygame.mouse.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    pantalla.fill((0, 0, 0))  
    pantalla.blit(texto, texto_rect)  
    pygame.draw.rect(pantalla, (0, 0, 0), boton_rect)    
    pantalla.blit(texto_boton, texto_rect1)
    pantalla.blit(texto_boton2,boton_rect2)
    pantalla.blit(texto_boton3,boton_rect4)

    if boton_rect.collidepoint(mouse) and clic[0]:
        pygame.quit()
        juego.jugar()
        sys.exit()
    if boton_rect2.collidepoint(mouse) and clic[0]:
        pygame.quit()
        #score.score()
        sys.exit()
    if boton_rect4.collidepoint(mouse) and clic [0]:
        pygame.quit()
        sys.exit()

    pygame.display.flip()

pygame.quit()
