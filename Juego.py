from enum import Flag
from tkinter import Y
import pygame, sys
from pygame.locals import*
import threading
pygame.init()
pygame.mixer.init()
import random

pygame.init()

#CONSTANTES 
ANCHO=1000
ALTO=550
COLOR_BG=(200,151,193)
NEGRO=(0,0,0)
BLANCO=(255, 255, 255)
COLOR=(154, 13, 176)

#VARIABLES 
flag = False

surface=pygame.display.set_mode((ANCHO, ALTO)) #VENTANA 
fondo=pygame.image.load ('fondo.jpeg').convert()
pygame.mixer.music.load ('maniacPiano2.mp3')
pygame.mixer.music.play(3)

pygame.display.set_caption("BP-Stray Kids: In Your Area")
canasta=pygame.image.load('canasta.png')
apple=pygame.image.load('pepino.png')
fresa= pygame.image.load('fresa.png')
roca=pygame.image.load('roca.png')


#Variables
canastaX= 40
canastaY=405
ancho = 170 - 40
alto = 140
velocidad=5
fresaX= 10
fresaY= 10
ancho_fr= 50
alto_fr=50
appleX = 20
appleY = 10
velA = 0.6
velF= 5
rocaX= 20
rocaY= 10
ancho_ro= 50
alto_ro=50
velr = 5
score=0
xm= 494
ym= 10
xs= 585
ys= 3
tam = 40
pu = ' SCORE: '
clock = pygame.time.Clock()
lim = 400
surface = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("BP-Stray Kids: In Your Area")
last_time = pygame.time.get_ticks()  # Inicialización de last_time


# Cargar imágenes y definir variables
fondo = pygame.image.load('fondo.jpeg').convert()
canasta = pygame.transform.scale(pygame.image.load('canasta.png'), (170, 140))
fresa = pygame.transform.scale(pygame.image.load('fresa.png'), (50, 50))
roca = pygame.transform.scale(pygame.image.load('roca.png'), (50, 50))

canastaX, canastaY = 40, 405
velocidad = 5
score = 0

clock = pygame.time.Clock()
last_time = pygame.time.get_ticks()

def marcador(surface, pu, tam, xm, ym): #FUNCION PARA EL MARCADOR 
    font = pygame.font.SysFont('Small Font', tam, bold=True)
    text_frame= font.render(pu, True, NEGRO, BLANCO)
    text_rect=text_frame.get_rect()
    text_rect.midtop=(xm, ym)
    surface.blit(text_frame, text_rect)

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, NEGRO)
    text_rect = text_surface.get_rect()
    text_rect.midtop=(x, y)
    surface.blit(text_surface, text_rect)

class MovingObject:
    def __init__(self, initial_x, initial_y, velocity):
        self.x = initial_x
        self.y = initial_y
        self.vel = velocity
        self.flag = False

    def move(self):
        while not self.flag:
            self.y += self.vel
            if self.y > 550:
                self.y = 0
                self.x = random.randint(4, 990)
            pygame.time.delay(10)  # Ajustar este valor si es necesario


#Eventos

# Crear instancias para los diferentes objetos en movimiento
fresa_obj = MovingObject(10, 10, 0.8)
roca_obj = MovingObject(20, 10, 0.8)
apple_obj = MovingObject(30, 10, 0.6)

# Crear hilos para mover los objetos
fresa_thread = threading.Thread(target=fresa_obj.move)
roca_thread = threading.Thread(target=roca_obj.move)
apple_thread = threading.Thread(target=apple_obj.move)


fresa_thread.start()
roca_thread.start()
apple_thread.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fresa_obj.flag = True
            roca_obj.flag = True
            apple_obj.flag = True
            pygame.quit()
            quit()

    surface.blit(fondo, (0, 0))
    surface.blit(canasta, (canastaX, canastaY))
    surface.blit(fresa, (fresa_obj.x, fresa_obj.y))
    surface.blit(roca, (roca_obj.x, roca_obj.y))
    surface.blit(apple, (apple_obj.x, apple_obj.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        canastaX -= velocidad
    if keys[pygame.K_RIGHT]:
        canastaX += velocidad

    # Lógica de colisiones y puntajes
    if fresa_obj.y > 444 and canastaX + 9 < fresa_obj.x < canastaX + ancho:
        score += 1
        fresa_obj.y = 0
        fresa_obj.x = random.randint(4, 990)
    if apple_obj.y > 444 and canastaX + 9 < roca_obj.x < canastaX + ancho:
        appleY +=velF 
        if appleY > 550:
            appleY = 0
            appleX= random.randint(4, 990)

    if roca_obj.y > 444 and canastaX + 9 < roca_obj.x < canastaX + ancho: 
            rocaY +=velr 
            if rocaY > 550:
             rocaY = 0
             rocaX= random.randint(4, 990)

    if rocaX > canastaX + 9: #Colision rocas
       if rocaX < canastaX + ancho:
        if rocaY > 444:
         flag= True


    if fresaX > canastaX + 9: #Colision Fresas
          if fresaX < canastaX + ancho:
            if fresaY > 444:
              score += 1
              fresaY = 0
              fresaX= random.randint(4, 990)

    if appleX > canastaX + 9: #Colision Fresas
          if appleX < canastaX + ancho:
            if appleY > 444:
              score += 10
              appleY = 0
              appleX= random.randint(4, 990)
    
    # Manejo de eventos del teclado para mover la canasta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        canastaX -= velocidad
    if keys[pygame.K_RIGHT]:
        canastaX += velocidad
             
    surface.blit (fondo, (0,0))
    surface.blit(canasta,(canastaX,canastaY))
    surface.blit(fresa,(fresaX,fresaY))
    surface.blit(roca,(rocaX,rocaY))
    marcador(surface, pu, tam, xm, ym)
    draw_text(surface,str(score),tam, xs,ys)
    pygame.display.update()

    fresa_thread.join()
    roca_thread.join()
    apple_thread.join()