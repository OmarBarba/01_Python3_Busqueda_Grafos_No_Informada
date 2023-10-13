# Búsqueda en Profundidad Iterativa (Iterative Deepening Depth-First Search - IDDFS)
def dls(graph, start, goal, max_depth):
    stack = [(start, [start])]  # Usamos una pila para nodos pendientes y sus rutas
    while stack:
        node, path = stack.pop()
        if len(path) > max_depth:
            continue  # Ignorar nodos más profundos que el límite actual
        if node == goal:
            return path  # Si encontramos el objetivo, devolvemos la ruta
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))  # Agregar vecinos no visitados

# función iddfs (Iterative Deepening Depth-First Search) realiza una búsqueda en profundidad iterativa. 
# Comienza con un límite de profundidad de 0 y, 
# en cada iteración, aumenta el límite de profundidad en 1.
#  Llama a la función dls con el nuevo límite de profundidad y devuelve la ruta si se encuentra una solución.

def iddfs(graph, start, goal): 
    depth = 0
    while True:
        result = dls(graph, start, goal, depth)
        if result:
            return result  # Devolver la ruta si se encontró
        depth += 1

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
result = iddfs(graph, start_node, goal_node)  # Llamada a la función IDDFS

if result:
    print("Ruta encontrada:")
    print(result)  # Imprimir la ruta encontrada
else:
    print("No se encontró una ruta.")
