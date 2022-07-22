class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        r, c = set(), set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
                    
        for i in range(rows):
            if i not in r: continue
            matrix[i] = [0] * cols
        
        for i in range(cols):
            if i not in c: continue
            for j in range(rows):
                matrix[j][i] = 0
        