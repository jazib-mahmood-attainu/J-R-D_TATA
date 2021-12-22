graph = dict() #{}

def addEdge(u,v,wt,Dir):#1 2 1 False
    if u not in graph:
        graph[u] = list()
    graph[u].append((v,wt))

    if not Dir: #Dir==False
        if v not in graph:
            graph[v] = list()
        graph[v].append((u,wt))

def bfs(src):
    visited = [False]*1000
    queue = []
    queue.append(src)
    visited[src] = True
    while len(queue)!=0:
        x = queue.pop(0)
        print(x)
        for neighbour,_ in graph[x]:
            if visited[neighbour] is False:
                queue.append(neighbour)
                visited[neighbour] = True
        



addEdge(0,2,1,False)
addEdge(0,3,1,False)
addEdge(0,1,1,False)
addEdge(2,3,1,False)
addEdge(3,1,1,False)

print(graph)

bfs(2)

