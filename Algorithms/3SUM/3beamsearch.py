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

def beam_search(graph, start, goal, beam_width):
    candidates = [(0, [start])]

    while candidates:
        candidates.sort(key=lambda x: x[0])
        new_candidates = []
        for _, path in candidates[:beam_width]:
            node = path[-1]
            if node == goal:
                return path

            neighbors = graph.get(node, [])
            for neighbor, edge_cost in neighbors:
                new_cost = sum(cost for _, cost in path) + edge_cost
                new_path = path + [(neighbor, edge_cost)]
                new_candidates.append((new_cost, new_path))

        candidates = new_candidates

    return None

# Example usage
start_node = 'A'
goal_node = 'G'
beam_width = 1
path = beam_search(graph, start_node, goal_node, beam_width)

if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join([node for node, _ in path])}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
