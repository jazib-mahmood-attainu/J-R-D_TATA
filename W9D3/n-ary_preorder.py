# import numpy as np
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
res = list()
class Solution:
    def preorder(self, root):
        global res
        if root.val == None:
            return
        cl = len(root.children)
        
        for i in range((cl)):
            print(root.children[i].val)
            if root.children[i]==None:
                continue
            res.extend([self.preorder(root.children[i])])
        return res
        