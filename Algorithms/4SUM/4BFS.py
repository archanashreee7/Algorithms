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
def best_first_search(graph, start, goal):
    open_list = [(0, [start])]
    while open_list:
        open_list.sort(key=lambda x: x[0])  # Sort by cost
        cost, path = open_list.pop(0)

        node = path[-1]
        if node == goal:
            return path

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in path:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                open_list.append((new_cost, new_path))

    return None

# Example usage
start_node = 'A'
goal_node = 'G'
path = best_first_search(graph, start_node, goal_node)
print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")


