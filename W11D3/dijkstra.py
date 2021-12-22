import heapq

graph = dict()

def addEdge(u,v,wt,Dir):#1 2 1 False
    if u not in graph:
        graph[u] = list()
    graph[u].append((v,wt))

    if not Dir: #Dir==False
        if v not in graph:
            graph[v] = list()
        graph[v].append((u,wt))


def SSSP(src,dest):#0,5
    
    n = 1000
    dist = [float("inf")]*n
    dist[src] = 0
    visited = [False]*n
    heap = list()

    heapq.heappush(heap,(0,src))

    while(len(heap)!=0):
        d,v = heapq.heappop(heap)
        visited[v]=True
        for neighbours,wt in graph[v]:#O(V)
            if not visited[neighbours] and dist[neighbours]>d+wt:
                dist[neighbours]=d+wt
                heapq.heappush(heap,(dist[neighbours],neighbours))#O()

    return dist[dest]


addEdge(1,2,1,False)
addEdge(1,0,22,False)

addEdge(0,3,10,False)
addEdge(2,3,8,False)
addEdge(2,5,133,False)

print(SSSP(0,5))