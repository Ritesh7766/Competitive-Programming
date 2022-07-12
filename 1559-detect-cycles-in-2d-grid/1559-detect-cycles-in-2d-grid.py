class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(node, color):
            stack = collections.deque()
            stack.appendleft((node, None))
            grid[node[0]][node[1]] = f'{color}v'
            
            while stack:
                u, parent = stack.popleft()
                adj_verts = [(u[0] + di, u[1] + dj) for di, dj in dir if (u[0] + di, u[1] + dj) != parent]
                for x, y in adj_verts:
                    if 0 <= x < rows and 0 <= y < cols:
                        if grid[x][y] == f'{color}v':
                            return True
                        elif grid[x][y] == color:
                            grid[x][y] = f'{color}v'
                            stack.appendleft(((x, y), u))
            return False
        
        for i in range(rows):
            for j in range(cols):
                if len(grid[i][j]) == 2: continue
                elif dfs((i, j), grid[i][j]):
                    return True
        return False
                