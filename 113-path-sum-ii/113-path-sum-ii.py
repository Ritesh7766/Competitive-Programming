# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        stack = collections.deque()
        stack.appendleft((root, root.val))
        parent, res = {root: None}, []
        
        while stack:
            u, sm = stack.popleft()
            if sm == targetSum and not u.left and not u.right: res.append(u)
            if u.left: 
                parent[u.left] = u
                stack.appendleft((u.left, sm + u.left.val))
            if u.right:
                parent[u.right] = u
                stack.appendleft((u.right, sm + u.right.val))
        
        paths = []
        for node in res:
            path = []
            while node:
                path.append(node.val)
                node = parent[node]
            paths.append(path[::-1])
        return paths