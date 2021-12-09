class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    lst = height(root.left)
    rst = height(root.right)
    return max(lst,rst)+1

def printNodesAtLevel(root,l):
    if root is None:
        return
    if l==1:
        print(root.data, end = " ")
        return

    printNodesAtLevel(root.left,l-1)
    printNodesAtLevel(root.right,l-1)
    



root = Node(50)
root.left = Node(60)
root.right = Node(100)
root.right.left = Node(20)
root.right.right = Node(80)
root.right.right.left = Node(90)
root.right.right.right = Node(105)


ht = height(root)
print("height of the tree is",ht)

for l in range(1,ht+1):
    printNodesAtLevel(root,l)
print()