class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
def printLL(head):
    cur = head
    while cur!=None:
        print(cur.data,end = " ")
        cur = cur.next
    print()


def rev_LL(head):
    prev = None
    cur = head
    while(cur!=None):
        nxt = cur.next

        cur.next = prev
        prev = cur
        cur = nxt

    return prev


head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)
head2.next.next.next.next = Node(10)

printLL(head2)

head2 = rev_LL(head2)

printLL(head2)
