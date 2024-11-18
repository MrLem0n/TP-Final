from nicegui import ui
import json
from arbolPrueba import raiz,simular_for


@ui.page('/')
def wea():
        with ui.row().classes('w-full items-center'):

            simular_for(raiz)
@ui.page('/episodios')
def eps():
     ui.label(f"Episodio: ")
     with ui.card().classes('w-full items-center'):
          ui.html()
ui.run()