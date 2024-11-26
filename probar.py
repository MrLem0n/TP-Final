from nicegui import ui
from arbolPrueba import raiz,simular_for
from listado import series  # Estructura del árbol de series y capítulos
from Contenido import contenidos
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'users')))
import login
from pruebaHeap import mostrar_top



@ui.page('/top')
def mejor():
    mostrar_top()

session_usuario = None
@ui.page('/login')
def logeando():
    login.loge()
    
@ui.page('/')
def pagina_principal():
    
        ui.page_title('Catalogo general')
        with ui.row().classes('w-full items-center'):
            ui.button('Series', on_click=lambda se='series': ui.navigate.to(f'/{se}'))
            ui.button('Peliculas', on_click=lambda asd='peliculas': ui.navigate.to(f'/{asd}'))
        with ui.row().classes('w-full items-center'):
            simular_for(raiz)

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
    ui.label("Catálogo de Series").classes("text-2xl font-bold mb-4")
    with ui.grid(columns=3).classes("gap-4"):
        for serie_nombre, nodo_serie in series.items():
            with ui.card().style("width: 300px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                ui.label(f"Serie: {serie_nombre}").classes("font-bold text-lg")
                ui.label(f"Número de capítulos: {len(nodo_serie.hijos)}")
                ui.button('Ver', on_click=lambda s=serie_nombre: ui.navigate.to(f'/{s}'))

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

# Ejecutar NiceGUI
ui.run()
