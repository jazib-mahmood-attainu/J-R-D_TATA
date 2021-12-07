class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

root = Node(20)
root.left = Node(5)
root.right = Node(7)
root.right.left = Node(8)
root.right.right = Node(9)

preorder(root)
