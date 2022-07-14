# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        elif not root.left and not root.right:
            return 1
        
        d1, d2 = inf, inf
        if root.left: d1 = self.minDepth(root.left)
        if root.right: d2 = self.minDepth(root.right)
        return min(d1, d2) + 1
        