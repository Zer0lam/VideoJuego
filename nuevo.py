from enum import Flag
from tkinter import Y
import pygame
import sys
import threading
from pygame.locals import *

pygame.init()
pygame.mixer.init()
import random

# CONSTANTES
ANCHO = 1000
ALTO = 550
COLOR_BG = (200, 151, 193)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
COLOR = (154, 13, 176)

# VARIABLES
flag = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False


surface = pygame.display.set_mode((ANCHO, ALTO))  # VENTANA
fondo = pygame.image.load('1.jpeg').convert()
pygame.mixer.music.load('maniacPiano2.mp3')
pygame.mixer.music.play(3)

pygame.display.set_caption("BP-Stray Kids: In Your Area")
canasta = pygame.image.load('canasta.png')
fresa = pygame.image.load('fresa.png')
roca = pygame.image.load('roca.png')
pepino = pygame.image.load('pepino.png')

# Variables
canastaX = 40
canastaY = 405
ancho = 170 - 40
alto = 140
velocidad = 4
fresaX = 10
fresaY = 10
ancho_fr = 50
alto_fr = 50
velF = 1
rocaX = 20
rocaY = 10
ancho_ro = 50
alto_ro = 50
velr = 1
score = 0
xm = 494
ym = 10
xs = 585
ys = 3
tam = 40
pu = ' SCORE: '
clock = pygame.time.Clock()
lim = 400
pepinoY = 10
pepinoX = 10
velP = 1 
fresas_recogidas = 15
rocas_recogidas = 0
pepinos_recogidos = 10



# IMAGENES (SE MOVERAN)
fresa = pygame.transform.scale(fresa, (50, 50))
roca = pygame.transform.scale(roca, (50, 50))
canasta = pygame.transform.scale(canasta, (170, 140))
pepino = pygame.transform.scale(pepino,(50,50))

# Cargar imágenes para contadores
imagen_fresa = pygame.image.load('fresa.png')
imagen_pepino = pygame.image.load('pepino.png')
imagen_fresa = pygame.transform.scale(imagen_fresa, (50, 50))  # Ajusta el tamaño según sea necesario
imagen_pepino = pygame.transform.scale(imagen_pepino, (50, 50))  # Ajusta el tamaño según sea necesario


def marcador(surface, pu, tam, xm, ym):  # FUNCION PARA EL MARCADOR
    font = pygame.font.SysFont('Small Font', tam, bold=True)
    text_frame = font.render(pu, True, NEGRO, BLANCO)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (xm, ym)
    surface.blit(text_frame, text_rect)


def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, NEGRO)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


# Creamos una clase para el hilo de la fresa
class HiloFresa(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global fresaX, fresaY, velF, flag, flag2
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)
            if flag2 == False:
                fresaY += velF
                if fresaY > ALTO:
                    fresaY = 0
                    fresaX = random.randint(0, ANCHO - ancho_fr)

            pygame.event.pump()

# Creamos una clase para el hilo de el pepino
class HiloPepino(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global pepinoX, pepinoY, velP, flag, flag3
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)
            if flag3 == False:
                pepinoY += velP
                if pepinoY > ALTO:
                    pepinoY = 0
                    pepinoX = random.randint(0, ANCHO - ancho_fr)

            pygame.event.pump()

# Creamos una clase para el hilo de la roca
class HiloRoca(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global rocaX, rocaY, velr, flag, flag3
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)
            if flag3 == False:
                rocaY += velr
                if rocaY > ALTO:
                    rocaY = 0
                    rocaX = random.randint(0, ANCHO - ancho_ro)

            pygame.event.pump()


# Iniciamos los hilos
hilo_fresa = HiloFresa()
hilo_roca = HiloRoca()
hilo_pepino = HiloPepino()
hilo_fresa.start()
hilo_roca.start()
hilo_pepino.start()


# Bucle principal
while not flag:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = True
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()
    
    # Movimiento continuo de la canasta
    if keys[K_RIGHT]:
        canastaX += velocidad
    if keys[K_LEFT]:
        canastaX -= velocidad

    # Restringe la posición de la canasta dentro de la pantalla
    canastaX = max(0, min(canastaX, ANCHO - ancho))

    if flag2 == False:  # Movimiento de la fresa cayendo
        fresaY += velF
        if fresaY > 550:
            fresaY = 0
            fresaX = random.randint(4, 990)

    if flag3 == False:  # Movimiento de la roca cayendo
        rocaY += velr
        if rocaY > 550:
            rocaY = 0
            rocaX = random.randint(4, 990)

    if flag4 == False:
        velP = random.uniform(0.5, 1.5)  # Velocidad aleatoria para el pepino
        pepinoY += velP
        if pepinoY > ALTO:
            pepinoY = 0
            pepinoX = random.randint(0, ANCHO - ancho_fr)

        # Colision rocas
        if rocaX > canastaX + 9 and rocaX < canastaX + ancho and rocaY > 444:
            score -= 1
            rocaY = 0
            rocaX = random.randint(4, 990)
            velr -=.1
            velF -=.1


    # Colision Fresas
    if fresaX > canastaX + 9 and fresaX < canastaX + ancho and fresaY > 444:
        score += 1
        fresas_recogidas -=1
        fresaY = 0
        fresaX = random.randint(4, 990)
        velF +=.1
        velr +=.1
        if fresas_recogidas == 0:
            hilo_fresa.sleep()

    # Colision Pepinos
    if pepinoX > canastaX + 9 and pepinoX < canastaX + ancho and pepinoY > canastaY:
        score += 10
        pepinos_recogidos -= 1
        pepinoY = 0
        pepinoX = random.randint(0, ANCHO - ancho_fr)
        velP += 0.3
        velF += 0.3
        velr += 0.3
        if pepinos_recogidos == 0:
            hilo_pepino.join()

    # Mostrar imágenes en lugar de texto
    surface.blit(fondo, (0, 0))
    surface.blit(canasta, (canastaX, canastaY))
    surface.blit(fresa, (fresaX, fresaY))
    surface.blit(roca, (rocaX, rocaY))
    surface.blit(pepino, (pepinoX, pepinoY))
    
    # Contadores en la esquina superior izquierda
    surface.blit(imagen_fresa, (10, 10))
    draw_text(surface, str(fresas_recogidas), tam, 70, 10)  # Número del contador de fresas
    
    surface.blit(imagen_pepino, (150, 10))
    draw_text(surface, str(pepinos_recogidos), tam, 210, 10)  # Número del contador de pepinos
    
    # Puntaje en el centro
    marcador(surface, pu + str(score), tam, ANCHO // 2, 10)

    pygame.display.update()


# Esperamos a que los hilos terminen antes de salir
hilo_fresa.join()
hilo_roca.join()
hilo_pepino.join()
