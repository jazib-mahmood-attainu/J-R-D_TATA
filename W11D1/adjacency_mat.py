n = 5
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

def addEdge(u,v,wt,Dir):#1 2 1 True
    graph[u][v]=wt
    if not Dir:
        graph[v][u]=wt
    

addEdge(1,2,1,True)
addEdge(0,3,1,True)
addEdge(2,3,1,True)
addEdge(3,2,1,True)
addEdge(2,5,1,True)

print(graph)