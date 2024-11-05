import json

class Contenido:
    def __init__(self,nombre,descripcion,tipo,duracion,categoria,popularidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.duracion = duracion 
        self.categoria = categoria
        self.popularidad = popularidad

    def __str__(self):
        return "Nombre: " + self.nombre + "\nDescripcion: " + self.descripcion + "\nTipo: " + self.tipo + "\nDuracion: " + self.duracion + "\nCategoria: " + self.categoria + "\nPopularidad: " + str(self.popularidad) + "\n"

# Abre el archivo JSON y carga los datos en una variable, codificacion UTF-8 para soportar caracteres especiales
with open("util/contents.json","r",encoding="utf-8") as file:
    data = json.load(file)

contenidos=[]


# Recorre los datos y crea un objeto Contenido para cada uno


for item in data:
    contenido = Contenido(
        nombre=item["nombre"],
        descripcion=item["descripcion"],
        tipo=item["tipo"],
        duracion=item["duracion"],
        categoria=item["categoria"],
        popularidad=item["popularidad"]
    )
    contenidos.append(contenido)

for contenido in contenidos:
    print(contenido)
    print()





