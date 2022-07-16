"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def trev(node, res = []):
            if not node:
                return res
            
            res.append(node.val)
            for v in node.children:
                res = trev(v, res)
            return res
        return trev(root)