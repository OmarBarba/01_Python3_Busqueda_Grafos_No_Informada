#Búsqueda en Profundidad Limitada (Depth-Limited Search - DLS)

def dls(graph, node, goal, depth, path):
    if depth == 0:
        return None  # Alcanzamos la profundidad límite sin encontrar el objetivo
    if node == goal:
        return path  # Hemos encontrado el objetivo, devolvemos la ruta

    if node not in path:
        path.append(node)  # Agregamos el nodo a la ruta
        for neighbor in graph.get(node, []):  # Obtenemos los vecinos del nodo actual
            result = dls(graph, neighbor, goal, depth - 1, path[:])  # Llamada recursiva
            if result is not None:
                return result  # Devolvemos la ruta si se encontró el objetivo en una llamada recursiva

    return None  # Si no se encontró el objetivo en esta rama, retornamos None

# Ejemplo de uso:
graph = {
    'A': ['B', 'C','J'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'                # Nodo de inicio
goal_node = 'E'                # Nodo objetivo
depth_limit = 3                # Profundidad máxima permitida
result = dls(graph, start_node, goal_node, depth_limit, [])  # Llamada a la función DLS

if result:
    print("Ruta encontrada:")
    print(result)  # Imprimir la ruta encontrada
else:
    print("No se encontró una ruta.")
