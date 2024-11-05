from nicegui import ui
from Contenido import contenidos,datos



# Obtener claves del primer elemento del JSON para definir las columnas
keys = datos[0].keys()
columns = [{"name": key, "label": key.capitalize(), "field": key} for key in keys]

def rend():
    ui.table(columns=columns, rows=datos, row_key='nombre')




