from Contenido import contenidos
from arbolPrueba import renderizar_contenido
from nicegui import ui

class NodoGeneral:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  # "serie", "temporada" o "episodio"
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.nombre}"

class ArbolGeneral:
    def __init__(self,raiz = None):
        self.raiz = raiz

    def agregar_serie(self, nombre_serie):
        serie = NodoGeneral(nombre_serie, "serie")
        if self.raiz is None:
            self.raiz = serie
        else:
            self.raiz.agregar_hijo(serie)
        print(f"Serie agregada: {serie}")
        print(f"Raíz actual: {self.raiz}")
        return serie

    def agregar_temporada(self, serie, nombre_temporada):
        temporada = NodoGeneral(nombre_temporada, "temporada")
        serie.agregar_hijo(temporada)
        print(f"Temporada agregada a {serie.nombre}: {temporada}")
        return temporada

    def agregar_episodio(self, temporada, nombre_episodio):
        episodio = NodoGeneral(nombre_episodio, "episodio")
        temporada.agregar_hijo(episodio)
        print(f"Episodio agregado a {temporada.nombre}: {episodio}")

    def iterar_nodos(self):
        if self.raiz is None:
            print("El árbol está vacío.")
            return
        nodos_por_visitar = [self.raiz]
        while nodos_por_visitar:
            nodo_actual = nodos_por_visitar.pop(0)
            yield nodo_actual
            nodos_por_visitar.extend(nodo_actual.hijos)
arbolito = ArbolGeneral()

# Verifica si la raíz ya ha sido configurada
if not arbolito.raiz and contenidos:
    contenido_inicial = contenidos[0]
    arbolito.raiz = NodoGeneral(contenido_inicial.nombre, contenido_inicial.tipo)

for contenido in contenidos[1:]:  # Empieza desde el segundo contenido
    if contenido.tipo == "Serie":
        serie_nodo = NodoGeneral(contenido.nombre, contenido.tipo)
        arbolito.raiz.agregar_hijo(serie_nodo)
        print(f"Se agregó la serie: {contenido.nombre}")
    else:
        print(f"Tipo no es 'Serie' para: {contenido.nombre}")
