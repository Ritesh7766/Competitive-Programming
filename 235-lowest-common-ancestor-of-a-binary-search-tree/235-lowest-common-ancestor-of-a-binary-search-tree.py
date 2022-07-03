# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        trev = root
        while trev:
            if trev.val > p.val and trev.val > q.val:
                trev = trev.left
            elif trev.val < p.val and trev.val < q.val:
                trev = trev.right
            else: break
        return trev