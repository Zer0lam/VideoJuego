import pygame
import time
import sys
import subprocess
import os

pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
FPS = 60

# Cargar imágenes para el icono
icono = pygame.image.load('BRAFP-27-11-2023.png')  # Reemplaza 'icono.png' con la ruta de tu archivo de icono


# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicialización de la pantalla
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("BRAF-P")
pygame.display.set_icon(icono)

# Tiempo de carga simulado (puedes cambiar esto según sea necesario)
tiempo_carga = 5  # en segundos

# Imagen de fondo
fondo = pygame.image.load('2.jpg')  # Reemplaza con la ruta de tu imagen
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Barra de progreso
barra_color = (255, 0, 0)
barra_radio = 10  # Radio de las esquinas redondeadas
barra_ancho = 400
barra_alto = 20
barra_x = (ANCHO - barra_ancho) // 2
barra_y = ALTO // 2 + 230  # Ajusta la posición vertical
barra_borde_grosor = 1

# Imágenes adicionales
imagen_superior = pygame.image.load('BRAFP-27-11-2023.png')
imagen_superior = pygame.transform.scale(imagen_superior, (470, 230))  # Ajusta el tamaño según sea necesario
imagen_superior_x = (ANCHO - imagen_superior.get_width()) // 2
imagen_superior_y = barra_y - 430  # Ajusta la posición vertical

# Imagen que sigue el recorrido de la barra
imagen_seguimiento = pygame.image.load('fresa.png')
imagen_seguimiento = pygame.transform.scale(imagen_seguimiento, (30, 30))  # Ajusta el tamaño según sea necesario

# Texto "Cargando..."
fuente = pygame.font.SysFont('calibri', 32)
texto_cargando = fuente.render('Cargando...', True, BLANCO)
texto_rect = texto_cargando.get_rect(center=(ANCHO // 2, barra_y - 10))  # Ajusta la posición vertical

# Porcentaje de carga
porcentaje_carga = 0

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()

# Bucle principal
cargando = True
tiempo_inicio = time.time()

while cargando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cargando = False
            pygame.quit()
            sys.exit()

    # Calcula el tiempo de carga transcurrido
    tiempo_transcurrido = time.time() - tiempo_inicio

    # Si ha pasado el tiempo de carga simulado, abre el nuevo script
    if tiempo_transcurrido >= tiempo_carga:
        # Abre el nuevo script
        subprocess.Popen("python menu.py")
        # Sale del bucle
        cargando = False
        # Si se ha pulsado la tecla ESC, cierra la pantalla de carga
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            cargando = False
            pygame.quit()
            sys.exit()

    # Simulación de carga 
    if porcentaje_carga < 100:
        porcentaje_carga += .5

    # Dibuja la pantalla de carga
    screen.blit(fondo, (0, 0))

    # Dibuja la imagen superior
    screen.blit(imagen_superior, (imagen_superior_x, imagen_superior_y))

    # Dibuja la barra redondeada y su borde exterior
    pygame.draw.rect(screen, BLANCO, (barra_x - barra_borde_grosor, barra_y - barra_borde_grosor, barra_ancho + 2 * barra_borde_grosor, barra_alto + 2 * barra_borde_grosor), border_radius=barra_radio)
    pygame.draw.rect(screen, barra_color, (barra_x, barra_y, porcentaje_carga / 100 * barra_ancho, barra_alto), border_radius=barra_radio)

    # Calcula la posición de la imagen de seguimiento
    imagen_x = barra_x + (porcentaje_carga / 100 * barra_ancho) - imagen_seguimiento.get_width() / 2

    # Dibuja la imagen de seguimiento directamente sobre la barra
    screen.blit(imagen_seguimiento, (imagen_x, barra_y - 5))

    # Dibuja el texto "Cargando..."
    screen.blit(texto_cargando, texto_rect)

    pygame.display.flip()
    reloj.tick(FPS)

