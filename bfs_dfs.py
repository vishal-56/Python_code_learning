def bfs(visited, graph,node):
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m,end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
            
graph = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
    }
visited = []
print("Breadth First Search:")
bfs(visited, graph, '5')
visited = []
print("\n\nDepth First Search")
dfs(visited, graph, '5')