# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth(node):
            if not node:
                return inf
            if not node.left and not node.right:
                return 1
            return min(min_depth(node.left), min_depth(node.right) ) + 1
        depth = min_depth(root)
        return 0 if depth is inf else depth