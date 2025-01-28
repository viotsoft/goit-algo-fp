import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()  # Множина для зберігання всіх вузлів

    def add_edge(self, from_node, to_node, weight):
        # Додаємо обидва вузли до множини
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

def dijkstra(graph, start):
    if start not in graph.nodes:
        return {}  # Стартовий вузол не існує
    
    # Ініціалізуємо відстані для всіх вузлів
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0

    heap = [(0, start)]
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        
        if current_node in visited:
            continue
        visited.add(current_node)

        # Перевіряємо наявність сусідів для поточного вузла
        for neighbor, weight in graph.edges.get(current_node, []):
            if neighbor not in distances:
                continue  # Захист на випадок помилок у даних
            
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Приклад використання:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")