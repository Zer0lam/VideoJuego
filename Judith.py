from pywinauto.application import Application

# Ruta a la aplicación Bloc de notas (Notepad)
app_path = "notepad.exe"

# Iniciar la aplicación
app = Application(backend="uia").start(app_path)
main_window = app.top_window()

# Escribir texto en Notepad
main_window.Edit.type_keys("Hola, este es un ejemplo de prueba funcional automatizada en Notepad.")

# Guardar el archivo
main_window.menu_select("Archivo->Guardar")
save_dialog = app.FileSaveAs
save_dialog.Edit.set_edit_text("archivo_de_prueba.txt")  # Nombre del archivo
save_dialog.Save.click()

# Cerrar Notepad
main_window.menu_select("Archivo->Salir")

# Esperar a que Notepad se cierre completamente
app.wait_not("visible")

# Finalizar la aplicación
app.kill()