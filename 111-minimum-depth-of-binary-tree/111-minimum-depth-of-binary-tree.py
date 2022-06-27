# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = collections.deque()
        queue.append((root, 1))
        
        while queue:
            u, depth = queue.popleft()
            if not u.left and not u.right: 
                return depth
            if u.left: queue.append((u.left, depth + 1))
            if u.right: queue.append((u.right, depth + 1))
        return 0