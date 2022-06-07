# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root)
        
        is_last_level = False
        while queue:
            u = queue.popleft()
            if (is_last_level and u.left) or (is_last_level and u.right):
                return False
            is_last_level = not u.left or not u.right or is_last_level
            if is_last_level and u.right: return False
            if u.left: queue.append(u.left)
            if u.right: queue.append(u.right)
        return True