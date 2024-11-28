from nicegui import ui
from arbolPrueba import raiz,simular_for
from listado import series  # Estructura del árbol de series y capítulos
from Contenido import contenidos
from db_users import usuarios
from grafo import grafo,generar_recomendaciones,dfs,bfs
from Heap import top
from registro import registrar
from watchlist import watchlist
session_usuario = None
background_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcxtj1-R7lh9ziN4YCJsV0gMPRVdg7gie9Mg&s"

@ui.page('/top')
def top5():
    ui.add_head_html(f'''
    <style>
        body {{
            background-image: url("https://img.freepik.com/fotos-premium/top-5-texto-3d_2227-1195.jpg");
            background-size: 50%;
            background-attachment: fixed;
            
        }}
       
    </style>
''')
    top()
@ui.page('/registro')
def registro():
    registrar()

@ui.page('/watchlist')
def pagina_wl():
    watchlist()
@ui.page('/')
def logeando():
    
    ui.add_head_html(f'''
    <style>
        body {{
            background-image: url("{background_image_url}");
            background-size: 50%;
            background-attachment: fixed;
            
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
            
            session_usuario= validar_login()
            ui.notify(f"Bienvenido, {session_usuario.nombre}!", color='green')
            ui.navigate.to('/catalogo')
            print(session_usuario)
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
    
@ui.page('/catalogo')
def pagina_principal():
    #validar que el usuario haya iniciado sesion
    if session_usuario:
        
        ui.page_title('Catalogo general')
        with ui.row().classes('w-full items-center'):
            ui.button('Series', on_click=lambda se='series': ui.navigate.to(f'/{se}'))
            ui.button('Peliculas', on_click=lambda asd='peliculas': ui.navigate.to(f'/{asd}'))
            ui.button('Recomendaciones', on_click=lambda username=session_usuario.nombre: ui.navigate.to(f'/{username}/recomendaciones')) 
            ui.label( f'Usuario actual: {session_usuario.nombre}').classes('ml-auto')
            
        with ui.row().classes('w-full items-center'):
            simular_for(raiz)
    else:
        ui.navigate.to('/')


@ui.page('/peliculas')
def pagina_peliculas():
    ui.page_title('Peliculas')
    for contenido in contenidos:
        if contenido.tipo == 'Película':
            with ui.row().classes('w-full items-center'):
                with ui.card().style("width: 300px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                    ui.label(f"Pelicula: {contenido.nombre}").classes("font-bold text-lg")
                    ui.label(f"Duración: {contenido.duracion} ")
                

# Página de series
@ui.page('/series')
def pagina_series():
    def agregar_usuario_historial(s):
        if session_usuario:
            ui.navigate.to(f'/{s}')
            if s not in session_usuario.historial:
                session_usuario.historial.append(s)
            print(f"historial de {session_usuario.nombre}: {session_usuario.historial}")
            
    ui.label("Catálogo de Series").classes("text-2xl font-bold mb-4")
    with ui.grid(columns=3).classes("gap-4"):
        for serie_nombre, nodo_serie in series.items():
            with ui.card().style("width: 300px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                ui.label(f"Serie: {serie_nombre}").classes("font-bold text-lg")
                ui.label(f"Número de capítulos: {len(nodo_serie.hijos)}")
                ui.button('Ver', on_click=lambda s=serie_nombre:agregar_usuario_historial(s) )

# Página de detalle de una serie
@ui.page('/{nombre}')
def detalle_serie(nombre: str):
    ui.label(f"Capítulos de: {nombre}").classes("text-2xl font-bold mb-4")
    
    serie_encontrada = False
    for serie_nombre, nodo_serie in series.items():
        if serie_nombre == nombre:
            serie_encontrada = True
            for hijo in nodo_serie.hijos:
                with ui.card().style("width: 700px; height: 500px; margin: 10px;").classes("hover:shadow-xl transition-shadow items-center"):
                    ui.label("Título: " + hijo.contenido.titulo).classes("font-bold text-lg")
                    ui.html(hijo.contenido.url)
            break  # Una vez encontrada, no es necesario seguir buscando

    if not serie_encontrada:
        ui.label(f"No se encontró la serie '{nombre}'.").classes("text-red-500")
@ui.page('/{username}/recomendaciones')
def recomendaciones():
    if session_usuario:
        with ui.column():  # Crear un contenedor en columna para mostrar los títulos
            ui.label(f"Recomendaciones para {session_usuario.nombre}:").classes("text-lg font-bold")
            
            recomendaciones = []  # Lista para almacenar las recomendaciones
            
            for wea in session_usuario.historial:
                for contenido in contenidos:
                    if wea == contenido.nombre:
                        # Obtener las recomendaciones como lista
                        recomendaciones.extend(generar_recomendaciones(contenido, grafo))
            
            # Evitar duplicados en las recomendaciones
            recomendaciones = list(set(recomendaciones))
            
            if recomendaciones:
                nodo_inicial = session_usuario.historial[0] if session_usuario.historial else None
                if nodo_inicial:
                    print("Recorrido DFS:")
                    dfs(grafo, nodo_inicial)
                    print("Recorrido BFS:")
                    bfs(grafo, nodo_inicial)
                else:
                    print("El historial del usuario está vacío.")
                ui.label(f'Basados en tu historial, recomendamos:')
                for titulo in recomendaciones:
                    with ui.row():
                        with ui.card().style("width: 300px; height: 300px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                            ui.label(titulo).classes("text-base font-medium")
                    
            else:
                ui.label("No hay recomendaciones disponibles.").classes("text-base text-gray-600")

            
            
ui.run()
