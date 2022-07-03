# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, mx = 0):
            if not node:
                return (-1, mx)
            h1, mx = diameter(node.left, mx)
            h2, mx = diameter(node.right, mx)
            mx = max(mx, h1 + h2 + 2)
            return (max(h1, h2) + 1, mx)
        return diameter(root)[1]