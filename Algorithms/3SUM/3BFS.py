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


