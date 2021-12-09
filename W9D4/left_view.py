class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def printNodes(root,cur_level,max_level):
    if root is None:
        return
    if cur_level>max_level[0]:
        print(root.data)
        max_level[0] = cur_level

    printNodes(root.left,cur_level+1,max_level)
    printNodes(root.right,cur_level+1,max_level)
    




root = Node(50)
root.left = Node(60)
root.right = Node(100)
root.right.left = Node(20)
root.right.right = Node(80)
root.right.right.left = Node(90)
root.right.right.right = Node(105)

max_level = [-1]
printNodes(root,0,max_level)