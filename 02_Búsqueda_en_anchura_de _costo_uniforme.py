#búsqueda en anchura costo uniforme Uniform Cost Search - UCS:

import heapq

def ucs(graph, start, goal):
    visited = set()                 # Conjunto para almacenar nodos visitados
    queue = [(0, start, [])]        # Cola de prioridad para nodos pendientes de exploración (costo, nodo, ruta)

    while queue:
        cost, node, path = heapq.heappop(queue)  # Obtener el nodo con el costo mínimo desde la cola
        if node not in visited:
            visited.add(node)         # Marcar el nodo como visitado
            if node == goal:          # Si el nodo actual es el objetivo, hemos encontrado una ruta
                return path + [node]  # Devolver la ruta completa desde el inicio hasta el objetivo
            neighbors = graph[node]   # Obtener los vecinos del nodo actual
            for neighbor, neighbor_cost in neighbors.items():
                if neighbor not in visited:
                    # Agregar vecinos no visitados a la cola de prioridad con su nuevo costo y ruta
                    heapq.heappush(queue, (cost + neighbor_cost, neighbor, path + [node]))

# Ejemplo de uso:
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'A': 5, 'F': 4},
    'D': {'B': 3},
    'E': {'B': 1, 'F': 6},
    'F': {'C': 4, 'E': 6}
}

start_node = 'A'                # Nodo de inicio
goal_node = 'F'                # Nodo objetivo
result = ucs(graph, start_node, goal_node)  # Llamada a la función UCS
print(result) 