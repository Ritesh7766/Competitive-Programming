class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        p_visited, a_visited = set(), set()
        
        def dfs(u, visited):
            visited.add(u)
            for di, dj in dir:
                x, y = di + u[0], dj + u[1]
                if 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and heights[x][y] >= heights[u[0]][u[1]]:
                    dfs((x, y), visited)
        
        for i in range(rows):
            dfs((i, 0), p_visited)
            dfs((i, cols - 1), a_visited)
            
        for i in range(cols):
            dfs((0, i), p_visited)
            dfs((rows - 1, i), a_visited)
            
        return p_visited & a_visited