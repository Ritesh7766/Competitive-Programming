class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1: return -1
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        queue = collections.deque()
        queue.append(((0, 0), 1) )
        grid[0][0] = 1
        
        while queue:
            u, depth = queue.popleft()
            if u[0] == n - 1 and u[1] == n - 1: return depth
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    queue.append(((x, y), depth + 1) )
                    grid[x][y] = 1
        
        return -1