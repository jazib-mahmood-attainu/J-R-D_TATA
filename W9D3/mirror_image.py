class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return 
    root.left,root.right = root.right,root.left
    mirror(root.left)
    mirror(root.right)
    return root

def preorder(root):
    if root == None:
        return
    print(root.data,end = " ")
    preorder(root.left)
    preorder(root.right)

    
root = Node(50)
root.left = Node(60)
root.right = Node(100)
root.right.left = Node(20)
root.right.right = Node(80)
root.right.right.left = Node(90)
root.right.right.right = Node(105)

preorder(root)
res = mirror(root)
print("***********")
preorder(res)


# print(ctr)
