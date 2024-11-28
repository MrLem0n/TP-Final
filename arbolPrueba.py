from Contenido import contenidos
from nicegui import ui

class Nodo:
    def __init__(self, contenido):
        self.izquierda = None
        self.derecha = None
        self.contenido = contenido

def insertar(raiz, contenido):
    if raiz is None:
        return Nodo(contenido)
    else:
        if contenido.popularidad < raiz.contenido.popularidad:
            raiz.izquierda = insertar(raiz.izquierda, contenido)
        else:
            raiz.derecha = insertar(raiz.derecha, contenido)
    return raiz

def en_orden(raiz):
    if raiz:
        en_orden(raiz.derecha)
        print(raiz.contenido, end="\n\n")
        en_orden(raiz.izquierda)

def agregar_contenido(contenidos):
    raiz = None
    for contenido in contenidos:
        raiz = insertar(raiz, contenido)
    return raiz

# Crear el árbol con los contenidos completos
raiz = agregar_contenido(contenidos)

#vamos a probar si funciona el renderizado:
def renderizar_contenido(contenidos):
        with ui.card().style("width: 400px; height: 500px; margin: 10px;").classes("hover:shadow-xl transition-shadow"):
                ui.label("Nombre: " + contenidos.nombre)
                ui.html('''
                                <style>
                                    .custom-img {
                                        width: 320px;
                                        border-radius: 10px;
                                        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                                        color: blue;
                                    }
                                </style>
                                <a href="https://youtu.be/xvFZjo5PgG0">
                                    <img src="https://i0.wp.com/codigoespagueti.com/wp-content/uploads/2023/08/Jojos-Bizarre-Adventure-Quien-es-el-personaje-mas-poderoso-compressed.jpg?fit=1280%2C720&amp;ssl=1" class="custom-img" />
                                </a>
                            ''')
                # ui.button('Ver', on_click=lambda c=contenido: agregar_wea(c.nombre))
                ui.label(f"Popularidad: {contenidos.popularidad}" )
                ui.label(f"Categorias: {contenidos.categoria}" )
# recorrerer el arbol:
                

def simular_for(raiz):
    pila = []
    nodo_actual = raiz

    while pila or nodo_actual:
        while nodo_actual:
            pila.append(nodo_actual)
            nodo_actual = nodo_actual.derecha
        nodo_actual = pila.pop()
        renderizar_contenido(nodo_actual.contenido)
        nodo_actual = nodo_actual.izquierda









    