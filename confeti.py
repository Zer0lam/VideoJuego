import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Confeti")

# Colores para el confeti
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Lista para almacenar los confetis
confeti = []

# Clase para representar cada confeti
class Confeti:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-height, 0)
        self.color = random.choice(colors)
        self.speed = random.randint(1, 5)

    def fall(self):
        self.y += self.speed
        if self.y > height:
            self.y = random.randint(-height, 0)
            self.x = random.randint(0, width)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 5, 5))  # Rectángulo para representar el confeti

# Bucle principal del juego
running = True
while running:
    screen.fill((255, 255, 255))  # Color de fondo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Crear nuevos confetis
    if len(confeti) < 100:  # Controlar la cantidad de confeti en pantalla
        confeti.append(Confeti())

    # Mostrar y hacer caer el confeti
    for c in confeti:
        c.fall()
        c.draw()

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Controlar la velocidad de actualización de la pantalla

pygame.quit()
