import heapq
from nicegui import ui
def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def watchlist():
    

    # Datos de ejemplo para la watchlist
    watchlist = {
        'Movie1': {'duration': 120, 'rating': 8.5},
        'Movie2': {'duration': 90, 'rating': 7.5},
        'Movie3': {'duration': 110, 'rating': 9.0},
    }

    # Crear un grafo basado en la duración (puedes cambiar a 'rating' u otra métrica)
    graph = {
        'Start': {'Movie1': watchlist['Movie1']['duration'], 'Movie2': watchlist['Movie2']['duration']},
        'Movie1': {'Movie3': watchlist['Movie3']['duration']},
        'Movie2': {'Movie3': watchlist['Movie3']['duration']},
        'Movie3': {}
    }

    # Función para construir la watchlist ordenada
    def build_watchlist():
        distances = dijkstra(graph, 'Start')
        ordered_watchlist = sorted(distances.items(), key=lambda x: x[1])
        return ordered_watchlist[1:]  # Excluir el nodo de inicio

    # UI con NiceGUI
    def main_page():
        ui.label('Watchlist Ordenada por Duración').classes('text-2xl font-bold mb-4')
        ordered_watchlist = build_watchlist()
        for movie, distance in ordered_watchlist:
            ui.label(f'{movie}: {distance} mins').classes('mb-2')
    with ui.row().classes('items-center justify-center w-full'):
        with ui.column().classes('items-center justify-center min-h-screen'):
            main_page()

