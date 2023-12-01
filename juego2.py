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
fondo = pygame.image.load('fondo.jpeg').convert()
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
velocidad = 2
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


# IMAGENES (SE MOVERAN)
fresa = pygame.transform.scale(fresa, (50, 50))
roca = pygame.transform.scale(roca, (50, 50))
canasta = pygame.transform.scale(canasta, (170, 140))
pepino = pygame.transform.scale(pepino,(50,50))


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
            clock.tick(60)  # Ajusta la velocidad del hilo a 60 fotogramas por segundo
            if flag2 == False:
                fresaY += velF
                if fresaY > 550:
                    fresaY = 0
                    fresaX = random.randint(4, 990)

            pygame.event.pump()

# Creamos una clase para el hilo de el pepino
class HiloPepino(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global pepinoX, pepinoY, velP, flag, flag3
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)  # Ajusta la velocidad del hilo a 60 fotogramas por segundo
            if flag2 == False:
                pepinoY += velF
                if pepinoY > 550:
                    pepinoY = 0
                    pepinoX = random.randint(4, 990)

            pygame.event.pump()

# Creamos una clase para el hilo de la roca
class HiloRoca(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global rocaX, rocaY, velr, flag, flag3
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)  # Ajusta la velocidad del hilo a 60 fotogramas por segundo
            if flag3 == False:
                rocaY += velr
                if rocaY > 550:
                    rocaY = 0
                    rocaX = random.randint(4, 990)

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

    if flag4 == False: #Movimiento del pepino cayendo
        # Modifica la velocidad de caída
        velP = random.randint(0, 2)
        if pepinoY > 550:
            pepinoY = 0
            pepinoX = random.randint(4, 990)

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
        fresaY = 0
        fresaX = random.randint(4, 990)
        velF +=.1
        velr +=.1

    # Colision Pepinos
    if pepinoX > canastaX + 9 and pepinoX < canastaX + ancho and pepinoY > 444:
        score += 10
        pepinoY = 0
        pepinoX = random.randint(4, 990)
        velP +=.3
        velF +=.3
        velr +=.3

    surface.blit(fondo, (0, 0))
    surface.blit(canasta, (canastaX, canastaY))
    surface.blit(fresa, (fresaX, fresaY))
    surface.blit(roca, (rocaX, rocaY))
    surface.blit(pepino,(pepinoX, pepinoY))
    marcador(surface, pu, tam, xm, ym)
    draw_text(surface, str(score), tam, xs, ys)
    pygame.display.update()


# Esperamos a que los hilos terminen antes de salir
hilo_fresa.join()
hilo_roca.join()
hilo_pepino.join()
