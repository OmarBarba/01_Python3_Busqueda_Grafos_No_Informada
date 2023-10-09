# búsqueda en anchura (BFS - Breadth-First Search)
from collections import deque

def bfs(graph, start, goal):
    visited = set()              # Conjunto para almacenar nodos visitados
    queue = deque([(start, [])])  # Cola para nodos pendientes de exploración, cada elemento es una tupla (nodo, ruta)

    while queue:
        node, path = queue.popleft()  # Obtener el primer nodo y su ruta desde la cola
        if node not in visited:
            visited.add(node)        # Marcar el nodo como visitado
            if node == goal:         # Si el nodo actual es el objetivo, hemos encontrado una ruta
                return path + [node]  # Devolver la ruta completa desde el inicio hasta el objetivo
            neighbors = graph[node]  # Obtener los vecinos del nodo actual
            for neighbor in neighbors:
                if neighbor not in visited:
                    # Agregar los vecinos no visitados a la cola con la nueva ruta
                    queue.append((neighbor, path + [node]))

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'                # Nodo de inicio
goal_node = 'F'                # Nodo objetivo
result = bfs(graph, start_node, goal_node)  # Llamada a la función de búsqueda
print(result)                   # Imprimir la ruta encontrada

