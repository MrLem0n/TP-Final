from Contenido import contenidos

# Crear el grafo como un diccionario
grafo={}




                
        





# Construir el grafo basado en similitudes por categoría
for i, item1 in enumerate(contenidos):
    for j, item2 in enumerate(contenidos):
        if i < j:  # Evitar comparaciones duplicadas
            # Verificar si comparten al menos una categoría
            if set(item1.categoria).intersection(item2.categoria):
                # Agregar la conexión bidireccional
                grafo.setdefault(item1.nombre, []).append(item2.nombre)
                grafo.setdefault(item2.nombre, []).append(item1.nombre)

# Función para generar recomendaciones
def generar_recomendaciones(contenido_objeto, grafo):
    contenido_nombre = contenido_objeto.nombre  # Extraemos el nombre para usarlo como clave del grafo
    if contenido_nombre not in grafo:
        return "No se encontraron recomendaciones para este contenido."
    
    # Generar recomendaciones basadas en los nodos conectados
    recomendaciones = grafo[contenido_nombre]
   
    return recomendaciones


