heap = [8,5,6,3,9,8,3,9,1,8]
def heapify(i):
    global heap
    left_idx = 2*i+1
    right_idx = 2*i+2

    if left_idx>=len(heap) and right_idx>=len(heap):
        return
    max_idx = i
    if left_idx<len(heap) and heap[i]<heap[left_idx]:
        max_idx = left_idx
    if right_idx<len(heap) and heap[max_idx]<heap[right_idx]:
        max_idx = right_idx

    if max_idx!=i:
        heap[max_idx],heap[i] = heap[i],heap[max_idx]
        heapify(max_idx)

n = len(heap)
for i in range(n-1,-1,-1):#[6,5,4,3,2,1,0]
    heapify(i)

def heapsort():
    global heap
    while len(heap)!=0:
        print(heap[0])
        heap[0],heap[-1] = heap[-1],heap[0]
        heap.pop()
        heapify(0)

heapsort()





