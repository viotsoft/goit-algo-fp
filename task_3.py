import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph.edges}
    distances[start] = 0
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from {start_node}: {shortest_paths}")

