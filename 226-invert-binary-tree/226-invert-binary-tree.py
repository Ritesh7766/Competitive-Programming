# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            u = queue.popleft()
            u.left, u.right = u.right, u.left
            if u.left: queue.append(u.left)
            if u.right: queue.append(u.right)
        return root