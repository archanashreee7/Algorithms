# Graph representation as an adjacency list with edge costs
graph = {
    'S': [('A', 1)],
    'A':[('B',3)],
    'B':[('C',1)],
    'C':[('G',1)],
    'B':[('G',1)],
    'S':[('D',5)],
    'D':[('G',1)],
    'G':[]
}


def depth_first_search(graph, node, goal, path=None):
    if path is None:
        path = []
    path = path + [node]

    if node == goal:
        return path

    if node not in graph:
        return None

    lowest_cost_path = None
    for neighbor in graph[node]:
        if neighbor not in path:
            new_path = depth_first_search(graph, neighbor, goal, path)
            if new_path:
                if lowest_cost_path is None or len(new_path) < len(lowest_cost_path):
                    lowest_cost_path = new_path

    return lowest_cost_path

# Example usage
start_node = 'D'
goal_node = 'G'
path = depth_first_search(graph, start_node, goal_node)

if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
