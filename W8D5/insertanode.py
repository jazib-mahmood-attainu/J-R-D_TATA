class Node:
    def __init__(self, val) :
        self.data = val
        self.next = None



head = None

def addNodeAtEnd(x):
    global head
    if head==None:
        head = Node(x)
        return
    cur = head
    while(cur.next!=None):
        cur = cur.next
    cur.next = Node(x)

def addNodeAtBeginning(x):
    global head
    if head == None:
        head = Node(x)
        return
    node = Node(x)
    node.next = head
    head = node

def addNodeAtKth(k,x):
    global head
    ctr = 1
    cur = head

    while(ctr<k-1):
        cur  = cur.next
        ctr += 1

    nn = Node(x)
    nn.next = cur.next
    cur.next = nn





def printLL():
    global head
    cur = head
    while cur!=None:
        print(cur.data)
        cur = cur.next




addNodeAtEnd(5)
addNodeAtEnd(6)
addNodeAtEnd(7)
addNodeAtEnd(8)

printLL()
print("**********")
addNodeAtBeginning(4)

printLL()

print("**********")
addNodeAtKth(3,5.5)
printLL()