class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: return image
        rows, cols = len(image), len(image[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        initial_color = image[sr][sc]
        
        def dfs(u):
            image[u[0]][u[1]] = color
            for di, dj in dir:
                x, y = u[0] + di, u[1] + dj
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == initial_color:
                    dfs((x, y) )
        
        dfs((sr, sc) )
        return image
            