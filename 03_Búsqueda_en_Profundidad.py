# Búsqueda en Profundidad (DFS - Depth-First Search)

class Graph:
    # Constructor de la clase
    def __init__(self):
        # Inicialización del diccionario que representará el grafo
        self.graph = {}

    # Método para agregar un vértice y sus vecinos
    def add_edge(self, vertex, neighbors):
        # Agregar el vértice y sus vecinos al grafo
        self.graph[vertex] = neighbors

    # Método para obtener los vecinos de un vértice
    def get_neighbors(self, vertex):
        # Retorna la lista de vecinos del vértice dado
        return self.graph[vertex]

# Crear una instancia de la clase Graph
graph = Graph()

# Agregar nodos (vértices) y conexiones (aristas) al grafo
graph.add_edge("A", ["B", "C"])
graph.add_edge("B", ["A", "D", "E"])
graph.add_edge("C", ["A", "F"])
graph.add_edge("D", ["B"])
graph.add_edge("E", ["B", "F"])
graph.add_edge("F", ["C", "E"])

# Mostrar el grafo
for vertex, neighbors in graph.graph.items():
    print(f"{vertex}: {neighbors}")