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
beam_width = 2
path = beam_search(graph, start_node, goal_node, beam_width)

if path:
    print(f"Path from {start_node} to {goal_node}: {' -> '.join([node for node, _ in path])}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
