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
