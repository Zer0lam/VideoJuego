from enum import Flag
from tkinter import Y #Comentario 
import pygame, sys
from pygame.locals import* # Import
pygame.init()
pygame.mixer.init() #se importa libreria para sonidos 
import random #random
#interfaz
#CONSTANTES #CONSTANTES
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
fresa= pygame.image.load('fresa.png')
roca=pygame.image.load('roca.png')


#Variables
canastaX= 40
canastaY=405
ancho = 170 - 40
alto = 140
velocidad=2
fresaX= 10
fresaY= 10
ancho_fr= 50
alto_fr=50
velF= 0.8
rocaX= 20
rocaY= 10
ancho_ro= 50
alto_ro=50
velr = 0.8
score=0
xm= 494
ym= 10
xs= 585
ys= 3
tam = 40
pu = ' SCORE: '
clock = pygame.time.Clock()
lim = 400


#IMAGENES (SE MOVERAN)
fresa=pygame.transform.scale(fresa,(50,50))
roca=pygame.transform.scale(roca,(50,50))
canasta=pygame.transform.scale(canasta,(170,140))

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
 
flag2= False
flag3= False

pygame.key.set_repeat(1, 10)
#Eventos
       

while not (flag):

    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            flag= True
            pygame.quit()
            sys.exit(0)

    if flag2 == False: #Movimiento de la fresa cayendo 
            fresaY +=velF 
            if fresaY > 550:
             fresaY = 0
             fresaX= random.randint(4, 990)

    if flag3 == False: #Movimiento de la roca cayendo 
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
             

   

           
    if evento.type==pygame.KEYDOWN:
            if evento.key==K_RIGHT:
                  canastaX+=velocidad
            if evento.key==K_LEFT:
                  canastaX-=velocidad 
            if evento.type==pygame.KEYUP:
             if (evento.key==pygame.K_LEFT or evento.key==pygame.K_RIGHT):
                 canastaX=0
                 

    surface.blit (fondo, (0,0))
    surface.blit(canasta,(canastaX,canastaY))
    surface.blit(fresa,(fresaX,fresaY))
    surface.blit(roca,(rocaX,rocaY))
    marcador(surface, pu, tam, xm, ym)
    draw_text(surface,str(score),tam, xs,ys)
    pygame.display.update()
