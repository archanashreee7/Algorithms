# Graph representation as an adjacency list with edge costs
graph = {
    'S': [('A', 4),('B', 6),('C',3)],
    'A':[('D',8),('E',7)],
    'D':[('K',2)],
    'E':[('M',5)],
    'K':[('M',1)],
    'M':[('O',4)],
    'O':[('G',5)],
    'B':[('F',4)],
    'F':[('O',3)],
    'B':[('G',7)],
    'C':[('H',9)],
    'H':[('G',2)],
    'C':[('J',8)],
    'J':[('R',5)],
    'R':[('T',3)],
    'J':[('T',4)],
}



def british_museum(graph, start, goal):
    # Initialize distances with infinity for all nodes except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize parents to reconstruct the path
    parents = {node: None for node in graph}

    # Queue for BFS traversal
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        for neighbor, edge_cost in graph.get(current_node, []):
            if distances[current_node] + edge_cost < distances[neighbor]:
                distances[neighbor] = distances[current_node] + edge_cost
                parents[neighbor] = current_node
                queue.append(neighbor)

    # Reconstruct the path from start to goal
    path = []
    current_node = goal
    while current_node:
        path.insert(0, current_node)
        current_node = parents[current_node]

    return path

# Example usage
start_node = 'A'
goal_node = 'G'
path = british_museum(graph, start_node, goal_node)

if path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
