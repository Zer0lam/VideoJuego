import pygame, sys, random
#CONSTANTES
WIDTH=500
HEIGHT=400
SIZE=(WIDTH,HEIGHT)
COLOR=(0,255,174)
RECT_COLOR=(0, 0, 0)
RECT_DIM=20
#VARIABLES
crash=False
pos_x=WIDTH//4*3
#FUNCIONES
def draw(pos_x):
    pygame.draw.rect(surface, RECT_COLOR,( pos_x,(HEIGHT//4*3), RECT_DIM, RECT_DIM))

#PROGRAMA
pygame.init()
surface=pygame.display.set_mode((SIZE))
pygame.display.set_caption("Collision")
while not(crash):
 for evento in pygame.event.get():
  if evento.type==pygame.QUIT:
   crash=True
 surface.fill(COLOR)
 draw(pos_x)
 pygame.display.update() 
pygame.quit()
sys.exit(0)

