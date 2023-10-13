#Búsqueda Bidireccional (Bidirectional Search)
def bidirectional_search(graph, start, goal):
    forward_visited = set()      # Conjunto para nodos visitados en la exploración desde el inicio
    backward_visited = set()     # Conjunto para nodos visitados en la exploración desde el objetivo
    forward_queue = [start]     # Cola para nodos pendientes en la exploración desde el inicio
    backward_queue = [goal]     # Cola para nodos pendientes en la exploración desde el objetivo

    while forward_queue and backward_queue:
        # Exploración desde el inicio
        forward_node = forward_queue.pop(0)  # Obtener el primer nodo de la cola
        forward_visited.add(forward_node)    # Marcar el nodo como visitado en la exploración desde el inicio

        # Exploración desde el objetivo
        backward_node = backward_queue.pop(0)  # Obtener el primer nodo de la cola
        backward_visited.add(backward_node)    # Marcar el nodo como visitado en la exploración desde el objetivo

        if forward_node in backward_visited:
            # Hemos encontrado una intersección, combinamos las rutas desde el inicio y el objetivo
            intersection = forward_node
            forward_path = [intersection]  # Inicializar la ruta desde la intersección hacia el inicio
            backward_path = [intersection]  # Inicializar la ruta desde la intersección hacia el objetivo

            while forward_node != start:
                forward_node = graph[forward_node][0]  # Acceder al primer vecino en la lista de vecinos
                forward_path.insert(0, forward_node)   # Insertar el nodo al principio de la ruta desde el inicio

            while backward_node != goal:
                backward_node = graph[backward_node][0]  # Acceder al primer vecino en la lista de vecinos
                backward_path.append(backward_node)     # Agregar el nodo al final de la ruta desde el objetivo

            return forward_path + backward_path  # Combinar ambas rutas para obtener la ruta completa

        # Expandir vecinos desde el inicio
        for neighbor in graph[forward_node]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)  # Agregar el vecino a la cola de exploración desde el inicio
                forward_visited.add(neighbor)   # Marcar el vecino como visitado en la exploración desde el inicio

        # Expandir vecinos desde el objetivo
        for neighbor in graph[backward_node]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)  # Agregar el vecino a la cola de exploración desde el objetivo
                backward_visited.add(neighbor)   # Marcar el vecino como visitado en la exploración desde el objetivo

    return None  # No se encontró una ruta

# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'                 # Nodo de inicio
goal_node = 'F'                 # Nodo objetivo
result = bidirectional_search(graph, start_node, goal_node)  # Llamada a la función de búsqueda bidireccional

if result:
    print("Ruta encontrada:")
    print(result)  # Imprimir la ruta encontrada
else:
    print("No se encontró una ruta.")  # Imprimir un mensaje si no se encontró una ruta
