import sqlite3
import pygame
import os
import sys
import menu

def crear_base_datos():
    conn = sqlite3.connect("puntuaciones.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS puntuaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def guardar_puntaje(nombre, score):
    conn = sqlite3.connect("puntuaciones.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO puntuaciones (nombre, score) VALUES (?, ?)", (nombre, score))
    conn.commit()
    conn.close()

def mostrar_puntajes():
    conn = sqlite3.connect("puntuaciones.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, score FROM puntuaciones ORDER BY score DESC LIMIT 10")
    datos = cursor.fetchall()
    conn.close()
    return datos

def mostrar_pantalla_scores():
    pygame.init()
    ventana = pygame.display.set_mode((450, 600))
    pygame.display.set_caption("Mejores Puntajes")
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
    reloj = pygame.time.Clock()
    fuente_titulo = pygame.font.Font("assets/font/KarmaticArcade-6Yrp1.ttf", 36)
    fuente_score = pygame.font.SysFont(None, 28)

    
    boton_volver = pygame.Rect(150, 520, 150, 40)
    texto_boton = fuente_score.render("VOLVER", True, (255, 255, 255))
    texto_boton_rect = texto_boton.get_rect(center=boton_volver.center)

    puntajes = mostrar_puntajes()

    run = True
    while run:
        mouse = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run = False

        ventana.blit(frames_fondo[indice_frame], (0, 0))
        indice_frame = (indice_frame + 1) % len(frames_fondo)

        
        titulo = fuente_titulo.render("TOP 10 PUNTAJES", True, (255, 255, 255))
        ventana.blit(titulo, (225 - titulo.get_width() // 2, 50))
        ventana.blit(texto_boton, texto_boton_rect)

        
        for i, (nombre, score_val) in enumerate(puntajes):
            texto = fuente_score.render(f"{i+1}. {nombre} - {score_val}", True, (255, 255, 255))
            ventana.blit(texto, (60, 120 + i * 35))

        if boton_volver.collidepoint(mouse) and clic[0]:
            pygame.quit()
            menu.menu_principal()
            sys.exit()

        pygame.display.flip()
        reloj.tick(25)

    pygame.quit()