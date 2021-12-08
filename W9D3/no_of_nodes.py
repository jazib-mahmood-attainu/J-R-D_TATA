class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None

# ctr = 0
# def inorder(root):
#     global ctr
#     if root == None:
#         return 0

#     inorder(root.left)
#     ctr+=1
#     inorder(root.right)

def no_of_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    lst = no_of_nodes(root.left)
    rst = no_of_nodes(root.right)
    return lst+rst+1


root = Node(50)
root.left = Node(60)
root.right = Node(100)
root.right.left = Node(20)
root.right.right = Node(80)
root.right.right.left = Node(90)
root.right.right.right = Node(105)

res = no_of_nodes(root)
print(res)
# print(ctr)
