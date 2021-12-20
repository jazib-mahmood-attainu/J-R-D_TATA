graph = dict() #{}

def addEdge(u,v,wt,Dir):#1 2 1 False
    if u not in graph:
        graph[u] = list()
    graph[u].append((v,wt))

    if not Dir: #Dir==False
        if v not in graph:
            graph[v] = list()
        graph[v].append((u,wt))

addEdge(1,2,1,False)
addEdge(0,3,1,False)
addEdge(2,3,1,False)
addEdge(3,2,1,False)
addEdge(2,5,1,False)

print(graph)