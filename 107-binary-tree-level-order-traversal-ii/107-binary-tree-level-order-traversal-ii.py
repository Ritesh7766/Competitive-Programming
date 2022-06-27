# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = collections.deque()
        
        while queue:
            level = []
            for _ in range(len(queue) ):
                u = queue.popleft()
                level.append(u.val)
                if u.left: queue.append(u.left)
                if u.right: queue.append(u.right)
            res.appendleft(level)
        return list(res)