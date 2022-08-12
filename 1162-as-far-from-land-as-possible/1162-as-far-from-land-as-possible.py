class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        queue = collections.deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append(((i, j), 0) )
        
        d = None
        while queue:
            u, d = queue.popleft()
            for di, dj in dir:
                x, y = u[0] + di, u[1] + dj
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    queue.append(((x, y), d + 1) )
        return d if d else -1