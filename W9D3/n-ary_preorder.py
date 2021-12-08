# import numpy as np
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        res2 = self.solve(root,res)
        return res2
    
    def solve(self,root,res):
        if root == None:
            return
        cl = len(root.children)
        print(root.val)
        res.append(root.val)
        print(cl,"******")
        for i in range(cl):
            self.solve(root.children[i],res)
        return res
        
        