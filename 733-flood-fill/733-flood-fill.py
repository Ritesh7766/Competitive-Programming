class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        rows, cols = len(image), len(image[0])
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        def dfs(u, initialColor):
            image[u[0]][u[1]] = newColor
            for di, dj in dir:
                x, y = u[0] + di, u[1] + dj
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == initialColor:
                    dfs((x, y), initialColor)
        
        dfs((sr, sc), image[sr][sc])
        
        return image