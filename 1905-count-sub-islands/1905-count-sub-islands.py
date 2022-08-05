class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(u, flg = False):
            flg = flg or not (grid1[u[0]][u[1]] == 1 and grid2[u[0]][u[1]] == 1)
            grid2[u[0]][u[1]] = 0
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < rows and 0 <= y < cols and grid2[x][y] == 1:
                    flg = dfs((x, y), flg)
            return flg
        
        sub_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if not dfs((i, j)): sub_islands += 1
        return sub_islands