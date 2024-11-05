from nicegui import ui
from prueba import usuarios
ui.add_head_html('''
<style>
body {
    background-color: #121212;
    color: #e0e0e0;
}
.ui-card, .ui-input, .ui-button {
    background-color: #1e1e1e;
    color: #e0e0e0;
    border: none;
}
.ui-input::placeholder {
    color: #e0e0e0;
}
</style>
''')


# Variable para almacenar el usuario de la sesión
session_usuario = None

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
nombre_input = ui.input(label='Usuario')
contraseña_input = ui.input(label='Contraseña', password=True)
ui.button("Iniciar sesión", on_click=login)
ui.run()