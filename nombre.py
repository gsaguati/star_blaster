import pygame
import os

def ingresar_nombre():
    pygame.init()
    width, height = 450, 600
    ventana = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Ingresar Nombre")
    pygame.mixer.music.load("assets/sonidos/base2.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)


    # Cargar fondo animado
    frames_fondo = []
    fondo = "assets/img/split"
    archivos = sorted(os.listdir(fondo))
    for archivo in archivos:
        if archivo.endswith(".jpg") and "frame" in archivo:
            ruta = os.path.join(fondo, archivo)
            imagen = pygame.image.load(ruta).convert()
            imagen = pygame.transform.scale(imagen, (450, 600))
            frames_fondo.append(imagen)

    fuente = pygame.font.SysFont(None, 40)
    input_activo = True
    nombre = ""
    indice_frame = 0
    fps_animacion = 25
    reloj = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if input_activo:
                    if event.key == pygame.K_RETURN:
                        if nombre.strip() != "":
                            return nombre
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    elif len(nombre) < 15:
                        nombre += event.unicode

        ventana.blit(frames_fondo[indice_frame], (0, 0))
        indice_frame = (indice_frame + 1) % len(frames_fondo)

        texto = fuente.render("Ingrese su nombre:", True, (255, 255, 255))
        ventana.blit(texto, (width//2 - texto.get_width()//2, 200))

        caja = pygame.Rect(width//2 - 100, 250, 200, 40)
        pygame.draw.rect(ventana, (0, 0, 0), caja)
        pygame.draw.rect(ventana, (255, 255, 255), caja, 2)

        texto_nombre = fuente.render(nombre, True, (255, 255, 255))
        ventana.blit(texto_nombre, (caja.x + 10, caja.y + 5))

        pygame.display.update()
        reloj.tick(fps_animacion)
