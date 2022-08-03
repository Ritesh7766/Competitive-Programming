class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(u, verts = 1):
            grid[u[0]][u[1]] = 2
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    verts = dfs((x, y), verts + 1)
            return verts
        
        mx_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    mx_area = max(mx_area, dfs((i, j)) )
        return mx_area