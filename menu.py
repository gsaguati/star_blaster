import pygame

pygame.init()
pantalla = pygame.display.set_mode((450, 600))
pygame.display.set_caption("Star Blaster")


fuente = pygame.font.Font("assets/font/KarmaticArcade-6Yrp1.ttf", 36)

texto = fuente.render("Star Blaster", True, (255, 255, 255))  
texto_rect = texto.get_rect(center=(225, 100)) 



run = True
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    pantalla.blit(texto, texto_rect)  
    pygame.display.flip()
    
pygame.quit()
