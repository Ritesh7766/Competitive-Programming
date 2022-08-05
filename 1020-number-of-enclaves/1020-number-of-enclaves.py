class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(u):
            grid[u[0]][u[1]] = 0
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    dfs((x, y))
                    
        for i in range(rows):
            if grid[i][0] == 1: dfs((i, 0))
            if grid[i][cols - 1] == 1: dfs((i, cols - 1))
                
        for j in range(cols):
            if grid[0][j] == 1: dfs((0, j))
            if grid[rows - 1][j] == 1: dfs((rows - 1, j))
        
        enclaves = 0
        for row in grid: enclaves += sum(row)
        return enclaves