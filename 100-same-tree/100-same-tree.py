# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append((p, q))
        
        while queue:
            u, v = queue.popleft()
            if not v and not u: continue
            elif u and not v or not u and v: return False
            elif u.val != v.val: return False
            queue.append((u.left, v.left))
            queue.append((u.right, v.right))
        return True