from nicegui import ui
from prueba import usuarios
def loge():
    


   
    

    # Función de validación de inicio de sesión
    def validar_login(usuario, contraseña):
        for usuario_registrado in usuarios:
            if usuario_registrado.nombre == usuario and usuario_registrado.contraseña == contraseña:
                return True
        return False

    # Función para iniciar sesión
    def login():
        global session_usuario
        nombre = nombre_input.value
        contraseña = contraseña_input.value
        if validar_login(nombre, contraseña):
            session_usuario = nombre
            ui.notify(f"Bienvenido, {nombre}!", color='green')
        else:
            ui.notify("Nombre de usuario o contraseña incorrectos", color='red')

    # Crear el formulario de inicio de sesión
    with ui.column().classes('items-center justify-center w-full min-h-screen'):
        with ui.row().classes('items-center justify-center w-full'):
              with ui.card().classes('items-center justify-center m-1/2 p-4 w-1/3 bg-red shadow-lg '):
                nombre_input = ui.input(label='Usuario')
                contraseña_input = ui.input(label='Contraseña', password=True)
                ui.button("Iniciar sesión", on_click=login)
