from nicegui import ui
from pruebaHeap import cargar_heap

def mostrar_top():
    heap = cargar_heap()
 #   for i in range(5):
    popular = heap.extraer_max()
    if popular:
         ui.label(f"Titulo: {popular[1]['titulo']}, Popularidad: {popular[0]}")




    

def top():
    with ui.column():
        ui.label("Top 5 Contenido Populares")
        mostrar_top()