import heapq

# Graph representation as an adjacency list with edge costs
graph = {
    'S': [('A',1)],
    'A':[('B',3)],
    'B':[('C',1)],
    'C':[('G',1)],
    'B':[('G',1)],
    'S':[('D',5)],
    'D':[('G',1)],
    'G':[]
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_cost in graph.get(current_node, []):
            distance = current_distance + edge_cost
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start, goal):
    path = []
    current_node = goal
    while current_node != start:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    path.insert(0, start)
    return path

# Example usage
start_node = 'A'
goal_node = 'G'
distances, predecessors = dijkstra(graph, start_node)

if distances[goal_node] != float('inf'):
    shortest_path = reconstruct_path(predecessors, start_node, goal_node)
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(shortest_path)}")
    print(f"Total cost: {distances[goal_node]}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
