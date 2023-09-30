def DFS(node,visited,graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

visited=set()
graph={
    'S':['A','B'],
    'A':['S','F'],
    'B':['S','C','D'],
    'D':['B','F'],
    'C':['B','E'],
    'E':['C','F'],
    'F':['A','D','E']
}
#recusion
DFS('A',visited,graph)
