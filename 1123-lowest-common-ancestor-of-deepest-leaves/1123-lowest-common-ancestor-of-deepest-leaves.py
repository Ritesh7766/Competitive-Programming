# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        parent, depth = {root : None}, {root : 0}
        queue = collections.deque()
        queue.append(root)
        
        height = 0
        while queue:
            u = queue.popleft()
            for v in [u.left, u.right]:
                if not v: continue
                queue.append(v)
                depth[v] = depth[u] + 1
                height = depth[v]
                parent[v] = u
        
        nodes = [u for u, d in depth.items() if d == height]
        if len(nodes) == 1: return nodes[0]
        lca, visited = None, set()
        
        mx_d = 0
        for node in nodes:
            d = 0
            while node and node not in visited:
                visited.add(node)
                node = parent[node]
                d += 1
            if node and d > mx_d: lca, mx_d = node, d
        return lca