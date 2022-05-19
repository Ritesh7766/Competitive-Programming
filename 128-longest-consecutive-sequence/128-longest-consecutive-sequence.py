class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Let each element be a vertex of a graph.
        # Each vertex v will be adjacent to at most two vertices, (v - 1) and (v + 1).
        visited = set()
        nums = set(nums)
        
        def dfs(node):
            stack = collections.deque()
            stack.appendleft(node)
            ln = 0
            
            while stack:
                u = stack.popleft()
                visited.add(u)
                ln += 1
                adj_vrts = [u - 1, u + 1]
                for v in adj_vrts:
                    if v in nums and v not in visited:
                        stack.appendleft(v)
            return ln
        
        mx_ln = 0
        for num in nums:
            if num not in visited:
                mx_ln = max(mx_ln, dfs(num))
        return mx_ln