class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Let each element be a vertex of a graph.
        # Each vertex v will be adjacent to at most two vertices, (v - 1) and (v + 1).
        visited = set()
        nums = set(nums)
        
        def dfs(u, ln = 1):
            visited.add(u)
            adj_verts = [u - 1, u + 1]
            for v in adj_verts:
                if v in nums and v not in visited:
                    ln = dfs(v, ln + 1)
            return ln
        
        mx_ln = 0
        for num in nums:
            if num not in visited:
                mx_ln = max(mx_ln, dfs(num))
        return mx_ln