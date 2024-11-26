
# **Documentación del Proyecto: Plataforma de Streaming**

## **Descripción General**
Este proyecto es una plataforma de streaming programada en Python que permite a los usuarios:
- Ver contenido como películas y series.
- Gestionar su historial de visualización.
- Recibir recomendaciones personalizadas basadas en categorías o popularidad.
- Explorar recomendaciones generadas mediante estructuras de datos avanzadas, como grafos y colas de prioridades.

Se utiliza NiceGUI como interfaz gráfica para proporcionar una experiencia interactiva y agradable para los usuarios.

---

## **Estructura del Proyecto**
El proyecto se organiza de la siguiente manera:

```
.
├── Contenido.py            # Modelo de datos para el contenido
├── Usuario.py              # Modelo de datos para el usuario
├── Grafo.py                # Funciones para gestionar el grafo de similitudes
├── ColaPrioridades.py      # Implementación de una cola de prioridades para recomendaciones
├── main.py                 # Archivo principal donde se configuran las rutas y la interfaz
├── templates/              # Archivos estáticos y estilos de NiceGUI (opcional)
└── datos.json              # Archivo JSON con los datos del contenido
```

---

## **Características Principales**

### 1. **Gestión de Contenido**
El contenido (series y películas) se define en un archivo `datos.json` con las siguientes claves:
- **nombre**: Título del contenido.
- **descripcion**: Breve descripción.
- **tipo**: Serie o película.
- **duracion**: Duración en minutos.
- **categoria**: Lista de géneros.
- **popularidad**: Puntuación de popularidad (0-100).

#### Clase `Contenido`
```python
class Contenido:
    def __init__(self, nombre, descripcion, tipo, duracion, categoria, popularidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tipo = tipo
        self.duracion = duracion
        self.categoria = categoria
        self.popularidad = popularidad
```

---

### 2. **Gestión de Usuarios**
Cada usuario tiene un perfil con:
- **Nombre, edad y correo electrónico**.
- **Historial de visualización**.
- **Watchlist personalizada**.

#### Clase `Usuario`
```python
class Usuario:
    def __init__(self, edad, nombre, correo, contraseña, historial):
        self.edad = edad
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.historial = historial
```

---

### 3. **Recomendaciones Personalizadas**

#### 3.1 Basadas en Categoría (Grafos)
- Cada contenido es un nodo en un grafo.
- Las conexiones (aristas) representan similitudes de categoría.
- Función `generar_recomendaciones`:
  - Dado un contenido, devuelve recomendaciones relacionadas según el grafo.

**Ejemplo de Grafo:**
```python
grafo = {
    "Breaking Bad": ["The Office", "Better Call Saul"],
    "Friends": ["How I Met Your Mother", "The Big Bang Theory"]
}
```

#### Código:
```python
def generar_recomendaciones(contenido, grafo):
    return grafo.get(contenido.nombre, [])
```

---

#### 3.2 Basadas en Popularidad (Cola de Prioridades)
- Se prioriza el contenido más popular para la watchlist del usuario.
- Implementado mediante un **Heap Binario** usando la clase `PriorityQueue`.

**Clase `PriorityQueue`:**
```python
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, contenido, prioridad):
        heapq.heappush(self.heap, (-prioridad, contenido))
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        return None
```

**Uso:**
```python
watchlist_queue = PriorityQueue()
for contenido in contenidos:
    watchlist_queue.push(contenido, contenido.popularidad)
```

---

### 4. **Interfaz Gráfica (NiceGUI)**
#### Configuración de Rutas
1. **Página de Inicio**:
   - Muestra información básica del usuario.
2. **Recomendaciones**:
   - Genera recomendaciones basadas en el historial.
   - Renderiza títulos de contenido en tarjetas.

#### Ejemplo de Ruta `/recomendaciones`:
```python
@ui.page('/{username}/recomendaciones')
def recomendaciones():
    if session_usuario:
        with ui.column():
            ui.label(f"Recomendaciones para {session_usuario.nombre}:").classes("text-lg font-bold my-4")
            for wea in session_usuario.historial:
                ui.label(f"Porque viste '{wea}', recomendamos:")
                recomendaciones = generar_recomendaciones(wea, grafo)
                for titulo in recomendaciones:
                    ui.card().tight().classes("my-2 p-4").with_content(
                        ui.label(titulo).classes("text-base")
                    )
```

---

## **Flujo de Trabajo**
1. **Cargar Datos del JSON**:
   - Leer el archivo `datos.json` y convertirlo en instancias de `Contenido`.
2. **Crear Grafos**:
   - Mapear las similitudes entre contenidos por categoría.
3. **Configurar Usuarios**:
   - Crear perfiles de usuario con historial y watchlist.
4. **Generar Recomendaciones**:
   - Usar el historial del usuario para sugerir contenido mediante grafos y colas.
5. **Renderizar Interfaz**:
   - Mostrar las recomendaciones dinámicamente con NiceGUI.

---

## **Requisitos del Sistema**
- **Python 3.10+**
- **Librerías**:
  - `heapq` (estándar para el manejo de heaps).
  - `NiceGUI` para la interfaz gráfica.
  - `json` para manejo de datos.

Instalación de dependencias:
```bash
pip install nicegui
```

---

## **Posibles Extensiones**
1. **Filtrar por Preferencias**:
   - Permitir que el usuario elija filtros como categoría o duración.
2. **Sistema de Votación**:
   - Agregar puntuaciones personales para mejorar las recomendaciones.
3. **Persistencia de Datos**:
   - Guardar el historial y las preferencias en un archivo o base de datos.

---

## **Créditos**
- **Desarrollador**: [Tu Nombre]
- **Fecha**: Noviembre 2024
