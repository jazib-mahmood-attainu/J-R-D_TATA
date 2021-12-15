import heapq

heap1 = []
heapq.heappush(heap1,2)
heapq.heappush(heap1,12)
heapq.heappush(heap1,222)
heapq.heappush(heap1,1)
heapq.heappush(heap1,5)

print(heap1)

x = heapq.heappop(heap1)
print(x)
print(heap1)

heap = [44,3,11,2,31,556,11]
heapq.heapify(heap)
print(heap)


heap2 = []


for i in range(5):
    v = int(input(f"Enter value to push in max heap {i+1}"))
    heapq.heappush(heap2,v*-1)

x = heapq.heappop(heap2)*-1
print(x)