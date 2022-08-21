class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        DP = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    DP[i][j] = 1 + DP[i + 1][j + 1]
                else:
                    DP[i][j] = max(DP[i + 1][j], DP[i][j + 1])
        
        return DP[0][0]