from Contenido import contenidos
from nicegui import ui
import json

class Capitulo:
    def __init__(self, episodio, titulo, url):
        self.episodio = episodio
        self.titulo = titulo
        self.url = url

    def __str__(self):
        return f"Episodio {self.episodio}: {self.titulo}\nURL: {self.url}"
    
class Nodo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return str(self.contenido)

# Crear un diccionario para las series (nodos raíz)
series = {}

# Crear nodos para las series
for contenido in contenidos:
    
    if contenido.tipo == "Serie":  # Asegúrate de que el tipo sea "serie"
        
        nodo_serie = Nodo(contenido)
        series[contenido.nombre] = nodo_serie
       
with open("util/episodios.json","r",encoding="utf-8") as file:
    datos = json.load(file)
# Agregar episodios como hijos de cada serie
for serie_nombre, episodios in datos.items():
    if serie_nombre in series:  # Verifica que la serie esté en el árbol
        for ep_data in episodios:
            capitulo = Capitulo(
                episodio=ep_data["episodio"],
                titulo=ep_data["titulo"],
                url=ep_data["url"]
            )
            nodo_capitulo = Nodo(capitulo)
            series[serie_nombre].agregar_hijo(nodo_capitulo)
            

# Imprimir el árbol para verificar
for serie_nombre, nodo_serie in series.items():
    print(f"Serie: {serie_nombre}")
    for hijo in nodo_serie.hijos:
        print(f"  {hijo.contenido.episodio}")
        print(f"  {hijo.contenido.url}")
        with ui.card().style("width: 400px; height: 500px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                ui.label("Nombre: " + hijo.contenido.titulo)
                ui.html(hijo.contenido.url)
ui.run()


