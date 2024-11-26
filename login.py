from nicegui import ui
from prueba import usuarios
background_image_url = 'https://cdn.discordapp.com/attachments/1179972089634115625/1310047904857325588/DALLE_2024-11-23_22.02.15_-_A_visually_striking_mosaic_of_movie_and_TV_series_covers_arranged_in_a_sleek_grid-based_streaming_platform_interface._Each_cover_displays_vibrant_an.webp?ex=6743ccb0&is=67427b30&hm=2314e2a5a63588409236b324f882ad7a5d7a21e57f802ec004b3b22074f44cbe&'

def loge():
    
    ui.add_head_html(f'''
    <style>
        body {{
            background-image: url("{background_image_url}");
            background-size: 50%;
            background-attachment: fixed;
            background-color: black;
            color: white;
        }}
       
    </style>
''')


    def validar_login():
        for usuario_registrado in usuarios:
            if usuario_registrado.nombre == nombre_input.value and usuario_registrado.contraseña == contraseña_input.value:
                return usuario_registrado
        return False

    # Función para iniciar sesión
    def login():
        global session_usuario
       
        if validar_login():
            session_usuario = validar_login()
            ui.notify(f"Bienvenido, {session_usuario.nombre}!", color='green')
            ui.navigate.to('/')
        else:
            ui.notify("Nombre de usuario o contraseña incorrectos", color='red')


   
    

   

    # Crear el formulario de inicio de sesión
    with ui.column().classes('items-center justify-center w-full min-h-screen'):
        with ui.row().classes('items-center justify-center w-full h-full'):
              with ui.card().classes('items-center justify-center m-1/2 p-4 w-1/6 h-96 bg-green-100 shadow-lg  '):
                ui.dark_mode()
                ui.image('img/user-circ.svg').classes('w-1/3 h-1/3')
                nombre_input = ui.input(label='Usuario')
                contraseña_input = ui.input(label='Contraseña', password=True)
                ui.button("Iniciar sesión", on_click=login)

    