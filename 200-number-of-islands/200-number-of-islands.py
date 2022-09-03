class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(u):
            grid[u[0]][u[1]] = '0'
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                    dfs((x, y) )
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1 
                    dfs((i, j) )
        return islands