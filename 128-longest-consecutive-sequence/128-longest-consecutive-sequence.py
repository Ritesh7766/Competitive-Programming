class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Let each element be a vertex of a graph.
        # Each vertex v will be adjacent to at most two vertices, (v - 1) and (v + 1).
        visited = set()
        nums = set(nums)
        
        def bfs(node):
            queue = collections.deque()
            queue.append(node)
            visited.add(node)
            ln = 0
            
            while queue:
                u = queue.popleft()
                ln += 1
                adj_vrts = [u - 1, u + 1]
                for v in adj_vrts:
                    if v in nums and v not in visited:
                        queue.append(v)
                        visited.add(v)
            return ln
        
        mx_ln = 0
        for num in nums:
            if num not in visited:
                mx_ln = max(mx_ln, bfs(num))
        return mx_ln