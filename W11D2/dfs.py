graph = dict() #{}

def addEdge(u,v,wt,Dir):#1 2 1 False
    if u not in graph:
        graph[u] = list()
    graph[u].append((v,wt))

    if not Dir: #Dir==False
        if v not in graph:
            graph[v] = list()
        graph[v].append((u,wt))

def dfs(src,visited):
    print(src)
    visited[src] = True
    for neighbour,_ in graph[src]:
        if visited[neighbour]==False: #if not visited[neighbour]
            dfs(neighbour,visited)



    


visited = [False]*100
addEdge(0,2,1,False)
addEdge(0,3,1,False)
addEdge(0,1,1,False)
addEdge(2,3,1,False)
addEdge(3,1,1,False)

print(graph)

dfs(2,visited)

