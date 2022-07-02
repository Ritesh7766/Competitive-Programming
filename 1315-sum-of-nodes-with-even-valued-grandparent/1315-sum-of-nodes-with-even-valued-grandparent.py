# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append((root, None, None))
        
        sm = 0
        while queue:
            u, parent, grandparent = queue.popleft()
            if grandparent and grandparent.val % 2 == 0:
                sm += u.val
            if u.left: queue.append((u.left, u, parent))
            if u.right: queue.append((u.right, u, parent))
        return sm