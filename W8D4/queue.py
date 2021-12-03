queue = list()

def enqueue(x):
    global queue
    queue.append(x)

def dequeue():
    global queue
    if isEmpty():
        return "Nothing in queue"
    x = queue.pop(0)
    return x

def isEmpty():
    global queue
    return len(queue)==0

enqueue(5)
enqueue(6)
enqueue(8)
print(dequeue())
print(queue)
print(dequeue())
print(queue)

print(dequeue())
print(dequeue())
print(queue)

