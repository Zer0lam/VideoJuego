import pygame
import sys
import pygame_gui
import subprocess

pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
FPS = 60

BLANCO = (255, 255, 255)

nombre_usuario = ""

# Cargar imágenes para el icono
icono = pygame.image.load('BRAFP-27-11-2023.png')  # Reemplaza 'icono.png' con la ruta de tu archivo de icono

# Inicialización de la pantalla
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Menú Principal")
pygame.display.set_icon(icono)

# Crear el objeto Manager para manejar la interfaz gráfica
manager = pygame_gui.UIManager((ANCHO, ALTO))

# Cargar imágenes
imagen_izquierda = pygame.image.load('letrero.png')
imagen_derecha = pygame.image.load('BRAFP-27-11-2023.png')
imagen_fondo = pygame.image.load('1.jpg')
imagen_boton = pygame.image.load('btnStart.png')

# Ajusta el tamaño según sea necesario
imagen_izquierda = pygame.transform.scale(imagen_izquierda, (230, 180)) 
imagen_derecha = pygame.transform.scale(imagen_derecha, (180, 95))

# Crear el botón con texto (puede cambiar el texto a una imagen más adelante)
boton_rect = pygame.Rect(ANCHO // 2 - 80, ALTO - 100, 140, 60)
boton = pygame_gui.elements.UIButton(relative_rect=boton_rect, text='', manager=manager)

# Crear el elemento UIImage con la imagen del botón
imagen_boton_rect = pygame.Rect(ANCHO // 2 - 100, ALTO - 180, 180, 220)
imagen_boton_elemento = pygame_gui.elements.UIImage(relative_rect=imagen_boton_rect, image_surface=imagen_boton, manager=manager)

# Configuración del cuadro de texto
cuadro_texto_rect = pygame.Rect(64, 115, 160, 35)
cuadro_texto = pygame_gui.elements.UITextEntryLine(
relative_rect=cuadro_texto_rect,
    manager=manager,
    object_id="cuadro_texto"
)
cuadro_texto.set_text_length_limit(20)  # Limita la longitud del texto
# Cambiar el color de la letra
cuadro_texto.text_color = pygame.Color(255, 255, 255)

# Configurar transparencia del cuadro de texto
cuadro_texto.background_colour.a=100  # Ajusta el componente alfa (transparencia)

# Establecer texto como placeholder
cuadro_texto.placeholder_text = "Ingresa tu usuario"

# Texto justo arriba del cuadro de texto
texto_arriba = "¡BIENVENIDO!"
fuente = pygame.font.SysFont(None, 35)
texto_renderizado = fuente.render(texto_arriba, True, (115, 71, 43, 1))
posicion_texto = (cuadro_texto_rect.x + cuadro_texto_rect.width // 2 - texto_renderizado.get_width() // 2,
                  cuadro_texto_rect.y - 30)

# Bucle principal
menu_activo = True
reloj = pygame.time.Clock()

while menu_activo:
    tiempo_delta = reloj.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_activo = False
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == boton:
                    # Al presionar el botón, actualiza la variable con el texto del cuadro
                    nombre_usuario = cuadro_texto.get_text()
                    subprocess.Popen("python Nivel1.py")
                    pygame.quit()
                    sys.exit()

        manager.process_events(event)

    manager.update(tiempo_delta)
    # Dibuja el fondo y las imágenes en la pantalla
    screen.blit(imagen_fondo, (0, 0))
    screen.blit(imagen_izquierda, (30, 0))
    screen.blit(imagen_derecha, (ANCHO - 180, 8))
    manager.draw_ui(screen)
    # Dibujar texto arriba del cuadro
    screen.blit(texto_renderizado, posicion_texto)

    pygame.display.flip()

pygame.quit()
sys.exit()
   