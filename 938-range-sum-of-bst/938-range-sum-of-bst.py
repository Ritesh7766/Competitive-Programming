# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = collections.deque()
        queue.append(root)
        
        sm = 0
        while queue:
            u = queue.popleft()
            if low <= u.val and u.val <= high:
                sm += u.val
            if u.left: queue.append(u.left)
            if u.right: queue.append(u.right)
        return sm