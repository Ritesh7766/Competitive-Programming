# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        
        def dfs(node):
            stack = collections.deque()
            stack.append(node)
            parent[node] = None
            
            while stack:
                u = stack.pop()
                adj_verts = [u.left, u.right]
                for v in adj_verts:
                    if not v: continue
                    stack.append(v)
                    parent[v] = u
        
        dfs(root)
        
        visited, trev = set(), p
        while p:
            visited.add(p)
            p = parent[p]
        
        while q:
            if q in visited:
                break
            q = parent[q]
            
        return q