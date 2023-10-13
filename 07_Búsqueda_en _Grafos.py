#Busqueda en grafos 

def graph_search(graph, start, goal, search_type='bfs'):
    visited = set()
    queue = [(start, [start])] if search_type == 'bfs' else []
    stack = [(start, [start])] if search_type == 'dfs' else []

    while queue or stack:
        if search_type == 'bfs':
            node, path = queue.pop(0)
        elif search_type == 'dfs':
            node, path = stack.pop()

        if node not in visited:
            visited.add(node)
            if node == goal:
                return path

            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    if search_type == 'bfs':
                        queue.append((neighbor, path + [neighbor]))
                    elif search_type == 'dfs':
                        stack.append((neighbor, path + [neighbor]))

    return None

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'  # Nodo de inicio
goal_node = 'F'   # Nodo objetivo
search_type = 'bfs'  # Puedes cambiar esto a 'dfs' para realizar una Búsqueda en Profundidad
result = graph_search(graph, start_node, goal_node, search_type)  # Llamada a la función de búsqueda en grafos

if result:
    print("Ruta encontrada:")
    print(result)  # Imprimir la ruta encontrada
else:
    print("No se encontró una ruta.")
