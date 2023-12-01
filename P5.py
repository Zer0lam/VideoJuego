
import pygame 

#Inicializar
pygame.init()

#Medidas
ANCHO = 800
ALTO=600

#Colores
BLANCO = (255, 255, 255)
NEGRO  = (0, 0, 0)
ROJO= (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#Ventana 
ventana = pygame.display.set_mode((ANCHO, ALTO))

#Datos
pos_x = 700
pos_y = 200

#Ciclo 
jugando = True

while jugando:

     
     #Eventos 
    for event in pygame.event.get():
         if event.type ==pygame.QUIT:
             jugando = False
         if event.type == pygame.K_ESCAPE: #KEYDOWN
             if event.key == pygame.KEYDOWN: #K_ESCAPE
                 jugando = False

#Logica 
    pos_x -= 1
    if pos_x <- ANCHO:
        pos_x = 0


#Dibujos 
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, ROJO, (pos_x, pos_y, 50, 50))
#ventana.fill(Negro)

#Actualizar 
    pygame.display.update()

    pygame.time.delay(4)

#Salir 
pygame.quit()








