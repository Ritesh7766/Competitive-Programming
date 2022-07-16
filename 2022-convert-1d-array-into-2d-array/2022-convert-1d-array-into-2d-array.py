class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        if m == 1: return [original]
        mat = [[0] * n for _ in range(m)]
        
        for i in range(len(original) ):
            mat[i // n][i % n] = original[i]
        return mat