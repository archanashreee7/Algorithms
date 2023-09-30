import collections
graph={
    'S':['A','B'],
    'A':['S','F'],
    'B':['S','C','D'],
    'D':['B','F'],
    'C':['B','E'],
    'E':['C','F'],
    'F':['A','D','E']
}
def bfs(g,root):
    queue=collections.deque([root])
    visited=[]
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.append(node)
        for item in g[node]:
            if item not in visited:
                queue.append(item)
                    
    print(visited)
bfs(graph,'S') 
