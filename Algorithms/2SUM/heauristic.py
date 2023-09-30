# Graph representation as an adjacency list
graph = {
    'S': ['A', 'B'],
    'A': ['S', 'F'],
    'B': ['S', 'C', 'D'],
    'D': ['B', 'F'],
    'C': ['B', 'E'],
    'E': ['C', 'F'],
    'F': ['A', 'D', 'E']
}

def heuristic(node, goal):
    # Uniform heuristic function (same for all nodes)
    return 1

def astar_search(graph, start, goal):
    open_list = [(start, [start], 0)]
    while open_list:
        node, path, cost_so_far = open_list.pop(0)

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            new_path = path + [neighbor]
            new_cost = cost_so_far + heuristic(neighbor, goal)
            open_list.append((neighbor, new_path, new_cost))

        # Sort the open list by the total cost (cost_so_far + heuristic)
        open_list.sort(key=lambda x: x[2] + heuristic(x[0], goal))

    return None

# Example usage
start_node = 'S'
goal_node = 'F'
path = astar_search(graph, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
