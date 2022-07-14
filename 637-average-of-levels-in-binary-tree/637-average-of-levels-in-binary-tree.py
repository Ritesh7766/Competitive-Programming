# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        
        res = []
        while queue:
            sm, cnt = 0, len(queue)
            for _ in range(cnt):
                u = queue.popleft()
                sm += u.val
                if u.left: queue.append(u.left)
                if u.right: queue.append(u.right)
            res.append(sm / cnt)
        return res