class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

head = Node(5)
print(head.data)
head.next = Node(6)
print(head.next.data)
head.next.next = Node(7)
print(head.next.next.data)
# head.next.next.next = Node(8)



