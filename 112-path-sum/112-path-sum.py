# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = collections.deque()
        stack.append((root, root.val))
        
        while stack:
            u, sm = stack.popleft()
            if sm == targetSum and not u.left and not u.right: return True
            if u.left: stack.appendleft((u.left, sm + u.left.val))
            if u.right: stack.appendleft((u.right, sm + u.right.val))
        return False