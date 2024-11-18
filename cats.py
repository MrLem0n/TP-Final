from Contenido import contenidos,Contenido
class Nodo:
    def __init__(self, contenido):
        self.contenido = contenido
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self, nivel=0):
        resultado = "\t" * nivel + f"- {self.contenido.nombre} ({self.contenido.tipo})\n"
        for hijo in self.hijos:
            resultado += hijo.__str__(nivel + 1)
        return resultado

# Construcción del árbol general
raiz = Nodo(Contenido("Catálogo de Contenidos", "Raíz del árbol", "raiz", "N/A", "N/A", 0))

series = {}

# Clasificar las series y capítulos
for contenido in contenidos:
    if contenido.tipo == "serie":
        nodo_serie = Nodo(contenido)
        series[contenido.nombre] = nodo_serie
        raiz.agregar_hijo(nodo_serie)
    elif contenido.tipo == "capitulo" and contenido.nombre.split(" - ")[0] in series:
        nombre_serie = contenido.nombre.split(" - ")[0]  # Suponiendo que el nombre del capítulo contiene el nombre de la serie
        nodo_capitulo = Nodo(contenido)
        series[nombre_serie].agregar_hijo(nodo_capitulo)

# Imprimir el árbol
# Imprimir diagnóstico de los nodos
for contenido in contenidos:
    print(f"Nombre: {contenido.nombre}, Tipo: {contenido.tipo}")

# Imprimir los nodos de series y capítulos para verificar que se están creando correctamente
print("Series en el árbol:")
for serie in series.values():
    print(serie.contenido.nombre)
    for capitulo in serie.hijos:
        print(f"\tCapítulo: {capitulo.contenido.nombre}")
