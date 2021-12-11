class Node:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None


def checkifValiBST(root):
    if root is None:
        return {
                "min_val":float("inf"),
                "max_val":float("-inf"),
                "isBST":True
                }

    if root.left is None and root.right is None:
        return {
                "min_val":root.data,
                "max_val":root.data,
                "isBST":True
                }

    left_ans = checkifValiBST(root.left) #returns a dictionary
    right_ans = checkifValiBST(root.right) #returns a dictionary

    if (left_ans["isBST"] is True) and (right_ans["isBST"] is True) and (left_ans["max_val"]<root.data and root.data<right_ans["min_val"]):
        return {
            "min_val":min(root.data,left_ans["min_val"]),
            "max_val":max(root.data,right_ans["max_val"]),
            "isBST":True
        }
    else:
        return {
            "min_val":min(root.data,left_ans["min_val"]),
            "max_val":max(root.data,right_ans["max_val"]),
            "isBST":False
        }
    


root = Node(50)
root.left = Node(6)
root.right = Node(100)
root.right.left = Node(70)
root.right.right = Node(180)
# root.right.right.right = Node(5)

res=checkifValiBST(root)
print(res["isBST"])

