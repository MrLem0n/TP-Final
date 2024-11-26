from conexion import obtener_contenido
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extraer_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self, indice):
        padre = (indice - 1)// 2
        if indice >0 and self.heap[indice][0] > self.heap[padre][0]:
            self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
            self._heapify_up(padre)

    def _heapify_down(self, indice):
        mayor = indice
        izquierdo = 2 * indice + 1
        derecho = 2 * indice + 2

        if izquierdo < len(self.heap) and self.heap[izquierdo][0] > self.heap[mayor][0]:
            mayor = izquierdo
        if derecho < len(self.heap) and self.heap[derecho][0] > self.heap[mayor][0]:
            mayor = derecho

        if mayor != indice:
            self.heap[indice], self.heap[mayor] = self.heap[mayor] = self.heap[mayor], self.heap[indice]
            self._heapify_down(mayor)

def cargar_heap():
    datos = obtener_contenido
    heap = MaxHeap  
    for item in datos:
        heap.insertar((item['popularidad'], item))
    return heap 