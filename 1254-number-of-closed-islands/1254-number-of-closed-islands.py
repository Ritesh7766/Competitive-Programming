class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        
        def bfs(u):
            queue = collections.deque()
            queue.append(u)
            grid[u[0]][u[1]] = 1
            flg = u[0] == 0 or u[0] == (rows - 1) or u[1] == 0 or u[1] == (cols - 1)
            
            while queue:
                u = queue.popleft()
                for di, dj in dir:
                    x, y = di + u[0], dj + u[1]
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                        if not flg: flg = x == 0 or x == (rows - 1) or y == 0 or y == (cols - 1)
                        grid[x][y] = 1
                        queue.append((x, y))
            return flg
        
        closed_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if not bfs((i, j)): closed_islands += 1
                        
        return closed_islands