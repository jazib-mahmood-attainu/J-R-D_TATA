class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    if root.left==None and root.right==None:
        print(root.data)
    inorder(root.right)


root = Node(50)
root.left = Node(60)
root.right = Node(100)
root.right.left = Node(20)
root.right.right = Node(80)
root.right.right.left = Node(90)
root.right.right.right = Node(105)

inorder(root)