import subprocess
from tkinter import Y
import pygame
import sys
import threading
from pygame.locals import *
import random
from pygame_gui import UIManager
from pygame_gui.elements.ui_window import UIWindow

# Inicialización de Pygame y otros módulos
pygame.init()
pygame.mixer.init()
pygame.font.init()

# CONSTANTES
ANCHO = 1000
ALTO = 550
COLOR_BG = (200, 151, 193)
NEGRO = (0, 0, 0)
BLANCO = (172, 172, 172)
COLOR = (154, 13, 176)

# VARIABLES
flag = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
# Cargar imágenes para el icono
icono = pygame.image.load('BRAFP-27-11-2023.png')  # Reemplaza 'icono.png' con la ruta de tu archivo de icono

# Crear una instancia de UIManager
manager = UIManager((ANCHO, ALTO))

surface = pygame.display.set_mode((ANCHO, ALTO))  # VENTANA
fondo = pygame.image.load('1.jpg').convert()
pygame.display.set_icon(icono)
pygame.mixer.music.load('maniacPiano2.mp3')
pygame.mixer.music.play(3)

pygame.display.set_caption("BP-Stray Kids: In Your Area")
canasta = pygame.image.load('canasta.png')
fresa = pygame.image.load('fresa.png')
roca = pygame.image.load('roca.png')
bananas = pygame.image.load('platano.png')

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
ym = 20
xs = 585
ys = 3
tam = 25
tam_Score = 40
tam_menu = 25
pu = ' Puntuación: '
fresas_menu = "7 Fresas"
platanos_menu="8 Bananas"
clock = pygame.time.Clock()
lim = 400
bananasY = 10
bananasX = 10
velP = 1 
rocas_recogidas = 0
fresas_recogidas = 0
fresas_faltantes = 7
fresas_faltantes_de = "/7"
bananas_recogidos = 0
bananas_faltantes = 8
bananas_faltantes_de = "/8"
barra_radio = 10
vida = 100
fin_juego = False  # Inicializar la variable fin_juego al comienzo del programa
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# IMAGENES (SE MOVERAN)
fresa = pygame.transform.scale(fresa, (50, 50))
roca = pygame.transform.scale(roca, (50, 50))
canasta = pygame.transform.scale(canasta, (170, 140))
bananas = pygame.transform.scale(bananas,(50,50))

# Cargar imágenes para contadores
imagen_fresa = pygame.image.load('fresa.png')
imagen_bananas = pygame.image.load('platano.png')
imagen_fresa = pygame.transform.scale(imagen_fresa, (40, 40))  # Ajusta el tamaño según sea necesario
imagen_bananas = pygame.transform.scale(imagen_bananas, (40, 40))  # Ajusta el tamaño según sea necesario
imagen_izquierda = pygame.image.load('BRAFP-27-11-2023.png')
imagen_izquierda = pygame.transform.scale(imagen_izquierda, (100, 60))

def marcador(surface, pu, tam_Score, xm, ym):  # FUNCION PARA EL MARCADOR
    font = pygame.font.SysFont('serif', tam_Score, bold=True)
    text_frame = font.render(pu, True, BLANCO)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (xm, ym)
    surface.blit(text_frame, text_rect)


def draw_text(surface, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, color)  # Utiliza el color proporcionado
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def dibujar_barra_vida(surface, x, y, vida_actual, vida_maxima):
    # Calcular el ancho de la barra de vida proporcional a la vida_actual y vida_maxima
    ancho_barra = int((vida_actual / vida_maxima) * 200)

    # Dibujar la barra de vida
    pygame.draw.rect(surface, (0, 0, 255), (x, y, ancho_barra, 20),border_radius=barra_radio)  # Barra azul
    pygame.draw.rect(surface, (0, 0, 0), (x + ancho_barra, y, 200 - ancho_barra, 20),border_radius=barra_radio)  # Barra negra restante
# Funciones para las pantallas de victoria y derrota

def pantalla_victoria_confeti():
    confeti_list = []

    class Confeti:
        def __init__(self):
            self.x = random.randint(0, ANCHO)
            self.y = random.randint(-ALTO, 0)
            self.color = random.choice(colors)
            self.speed = random.randint(1, 5)

        def fall(self):
            self.y += self.speed
            if self.y > ALTO:
                self.y = random.randint(-ALTO, 0)
                self.x = random.randint(0, ANCHO)

        def draw(self):
            pygame.draw.rect(surface, self.color, (self.x, self.y, 5, 5))

    for _ in range(200):
        confeti_list.append(Confeti())

    # Dibujar fondo gris semitransparente
    fondo_victoria = pygame.Surface((700, 450), pygame.SRCALPHA)
    pygame.draw.rect(fondo_victoria, (243, 243, 243, 170), (300, 100, 500, 600))

    # Dibujar texto, imágenes y contadores
    draw_text(fondo_victoria, "¡Victoria!", 60, ANCHO // 2, 160)
    draw_text(fondo_victoria, f"Puntuación: {score}", 30, ANCHO // 2, 260)
    draw_text(fondo_victoria, "Presiona SPACE para continuar", 30, ANCHO // 2, 400)

    running = True
    clock = pygame.time.Clock()
    space_pressed = False  # Variable para controlar si se ha presionado la barra de espacio

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                if space_pressed:
                    subprocess.Popen("python Nivel2.py")
                    running = False  # Cambia esta lógica según sea necesario

        surface.fill((255, 255, 255))
        surface.blit(fondo, (0, 0))
        surface.blit(fondo_victoria, (0, 0))
        for c in confeti_list:
            c.fall()
            c.draw()
        

        pygame.display.flip()
        clock.tick(60)

    pygame.time.delay(3000)  # Esperar 3000 milisegundos (3 segundos) antes de salir
    pygame.quit()  # Cerrar Pygame
    sys.exit()     # Salir del programa

def pantalla_derrota():
    global score, fresas_faltantes, bananas_faltantes, vida, fresas_recogidas, bananas_recogidos, velr, velF, velP
    # Dibujar fondo gris semitransparente
    fondo_derrota = pygame.Surface((700, 450), pygame.SRCALPHA)
    pygame.draw.rect(fondo_derrota, (243, 243, 243, 170), (300, 100, 500, 600))

    # Dibujar texto, imágenes y contadores
    draw_text(fondo_derrota, "¡Derrota!", 60, ANCHO // 2, 160)
    draw_text(fondo_derrota, f"Puntuación: {score}", 30, ANCHO // 2, 260)
    draw_text(fondo_derrota, "Presiona SPACE para reiniciar", 30, ANCHO // 2, 400)

    running = True
    clock = pygame.time.Clock()
    space_pressed = False  # Variable para controlar si se ha presionado la barra de espacio

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                if space_pressed:
                   # Reiniciar el nivel
                    score = 0
                    fresas_faltantes = 7
                    fresas_recogidas = 0
                    bananas_faltantes = 8
                    bananas_recogidos = 0
                    velF = 1
                    velP = 1
                    velr = 1
                    vida = 100
                    return
        
        surface.fill((255, 255, 255))
        surface.blit(fondo, (0, 0))
        surface.blit(fondo_derrota, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.time.delay(3000)  # Esperar 3000 milisegundos (3 segundos) antes de salir
    pygame.quit()  # Cerrar Pygame
    sys.exit()     # Salir del programa

# Semáforo para asegurar la actualización segura de variables compartidas
mutex = threading.Lock()

# Creamos una clase base para los hilos
class HiloBase(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global flag
        clock = pygame.time.Clock()
        while not flag:
            clock.tick(60)
            with mutex:  # Usar el semáforo
                self.move_logic()

    def move_logic(self):
        pass

# Creamos una clase para el hilo de la fresa
class HiloFresa(HiloBase):
    def __init__(self):
        super().__init__()

    def move_logic(self):
        global fresaX, fresaY, velF
        fresaY += velF
        if fresaY > 550:
            fresaY = 0
            fresaX = random.randint(4, 990)

# Creamos una clase para el hilo de el bananas
class Hilobananas(HiloBase):
    def __init__(self):
        super().__init__()

    def move_logic(self):
        global bananasX, bananasY, velP
        bananasY += velP
        if bananasY > ALTO:
            bananasY = 0
            bananasX = random.randint(0, ANCHO - ancho_fr)

# Creamos una clase para el hilo de la roca
class HiloRoca(HiloBase):
    def __init__(self):
        super().__init__()

    def move_logic(self):
        global rocaX, rocaY, velr
        rocaY += velF
        if rocaY > 550:
            rocaY = 0
            rocaX = random.randint(4, 990)


# Iniciamos los hilos
hilo_fresa = HiloFresa()
hilo_roca = HiloRoca()
hilo_bananas = Hilobananas()
hilo_fresa.start()
hilo_roca.start()
hilo_bananas.start()

# Variable para determinar si se está mostrando la pantalla de inicio
mostrando_pantalla_inicio = True

# Bucle principal
while not flag:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = True

    keys = pygame.key.get_pressed()

    # Mostrar la pantalla de inicio antes de iniciar el juego
    if mostrando_pantalla_inicio:
        surface.blit(fondo, (0, 0))
        # Dibujar fondo gris semitransparente
        fondo_inicio = pygame.Surface((700, 450), pygame.SRCALPHA)
        pygame.draw.rect(fondo_inicio, (243, 243, 243, 170), (300, 100, 500, 600))

        # Dibujar texto, imágenes y contadores
        draw_text(fondo_inicio, "NIVEL 1", 60, ANCHO // 2, 160)
        draw_text(fondo_inicio, "Debes recolectar: ", 20, ANCHO // 2, 220)
        draw_text(fondo_inicio, "Presiona SPACE para empezar", 30, ANCHO // 2, 400)
        
        # Dibujar la pantalla de inicio sobre la pantalla principal
        surface.blit(fondo_inicio, (0, 0))
        # ... (dibuja otras imágenes y contadores según sea necesario)
        surface.blit(imagen_fresa, (400, 250))
        draw_text(surface, str(fresas_menu), tam_menu, 500, 260,(219, 46, 64, 1))
        surface.blit(imagen_bananas, (400, 310))
        draw_text(surface, str(platanos_menu), tam_menu, 510, 320,(252, 212, 98, 1))

        # Actualizar la pantalla
        pygame.display.flip()

        # Verificar si se presiona la tecla SPACE para empezar el juego
        if keys[K_SPACE]:
            mostrando_pantalla_inicio = False

    else:
    
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
            velP = random.uniform(0.5, 1.5)  # Velocidad aleatoria para el bananas
            bananasY += velP
            if bananasY > ALTO:
                bananasY = 0
                bananasX = random.randint(0, ANCHO - ancho_fr)

            # Colision rocas
            if rocaX > canastaX + 9 and rocaX < canastaX + ancho and rocaY > 444:
                with mutex:  # Usar el semáforo
                    vida -= 33
                    score -= 1
                    rocaY = 0
                    rocaX = random.randint(4, 990)
                    if score <= 0:
                        score = 0  # Asegurarse de que el contador no sea negativo
                    velr -= 0.1
                    velF -= 0.1
                    velP -= 0.1
                    if vida <= 0:
                        pantalla_derrota()

        # Colision Fresas
        if fresaX > canastaX + 9 and fresaX < canastaX + ancho and fresaY > 444:
            score += 1
            fresas_recogidas +=1
            fresas_faltantes -= 1
            if fresas_faltantes <= 0:
                fresas_faltantes = 0  # Asegurarse de que el contador no sea negativo
            fresaY = 0
            fresaX = random.randint(4, 990)
            velF += 0.1
            velr += 0.1
            velP += 0.1

        # Colision bananass
        if bananasX > canastaX + 9 and bananasX < canastaX + ancho and bananasY > canastaY:
            score += 1
            bananas_recogidos +=1
            bananas_faltantes -= 1
            
            if bananas_faltantes <= 0:
                bananas_faltantes = 0  # Asegurarse de que el contador no sea negativo
            bananasY = 0
            bananasX = random.randint(0, ANCHO - ancho_fr)
            velP += 0.3
            velF += 0.3
            velr += 0.3 

        # Mostrar imágenes en lugar de texto
        surface.blit(fondo, (0, 0))
        surface.blit(canasta, (canastaX, canastaY))
        surface.blit(fresa, (fresaX, fresaY))
        surface.blit(roca, (rocaX, rocaY))
        surface.blit(bananas, (bananasX, bananasY))
        surface.blit(imagen_izquierda, (10, 10))

        # Dibuja la barra de vida
        dibujar_barra_vida(surface, 10, 150, vida, 100)

        # Contadores y puntaje
        surface.blit(imagen_fresa, (10, 70))
        draw_text(surface, str(fresas_recogidas), tam, 60, 70)
        draw_text(surface, str(fresas_faltantes_de), tam, 80, 70)
        surface.blit(imagen_bananas, (10, 110))
        draw_text(surface, str(bananas_recogidos), tam, 60, 110)
        draw_text(surface, str(bananas_faltantes_de), tam, 80, 110)

        marcador(surface, pu + str(score), tam, ANCHO // 2, 50)

        # Verificar si ambos contadores han llegado a 0
        if fresas_faltantes <= 0 and bananas_faltantes <= 0:
            pantalla_victoria_confeti()

    # Actualizar y dibujar la interfaz gráfica
    manager.update(0.01)
    manager.draw_ui(surface)
    pygame.display.update()

# Esperar a que los hilos terminen antes de salir
hilo_fresa.join()
hilo_roca.join()
hilo_bananas.join()

# Salir de Pygame
pygame.quit()
sys.exit(0)

