class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        DP = [0] * (n + 1)
        DP[0], DP[1] = 0, 1
        for i in range(2, n + 1):
            DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]
        return DP[n]