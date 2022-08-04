class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def bfs(node):
            queue = collections.deque()
            queue.append(node)
            grid[node[0]][node[1]] = 1
            flg = node[0] == 0 or node[0] == (rows - 1) or node[1] == 0 or node[1] == (cols - 1)
            
            while queue:
                u = queue.popleft()
                for di, dj in dir:
                    x, y = di + u[0], dj + u[1]
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                        flg = flg or x == 0 or x == (rows - 1) or y == 0 or y == (cols - 1)
                        grid[x][y] = 1
                        queue.append((x, y))
            return flg
        
        closed_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if not bfs((i, j)):
                        closed_islands += 1
        return closed_islands
                    