def british_museum_search(graph, start_node, goal_node):
    queue = []
    queue.append([start_node])  # Use a list to store the path instead of just the current node

    visited = set()
    visited.add(start_node)

    while queue:
        path = queue.pop(0)
        current_node = path[-1]

        if current_node == goal_node:
            return path  # Return the complete path if the goal is reached

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)  # Create a new path to avoid modifying the original
                new_path.append(neighbor)
                queue.append(new_path)

    return []  # Return an empty list if no path is found

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'F'],
    'B': ['S', 'C', 'D'],
    'D': ['B', 'F'],
    'C': ['B', 'E'],
    'E': ['C', 'F'],
    'F': ['A', 'D', 'E']
}

start_node = 'S'
goal_node = 'F'
path = british_museum_search(graph, start_node, goal_node)
print(path)
