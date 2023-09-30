def beam_search(graph, start_node, goal_node, beam_width):
    queue = [(start_node, 0)]
    closed_set = set()
    while queue:
        node, cost = queue.pop(0)
        if node == goal_node:
            return [node]
        closed_set.add(node)
        for neighbor in graph[node]:
            if neighbor not in closed_set:
                queue.append((neighbor, cost + 1))
        if len(queue) == beam_width:
            worst_cost = queue.pop(0)
            if worst_cost != 0:
                closed_set.remove(worst_cost)
    return None
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
beam_width= 1
path = beam_search(graph, start_node, goal_node, beam_width)
print(path)
