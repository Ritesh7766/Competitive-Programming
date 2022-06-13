class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 1, 2, 0
        if n == 1: return a
        elif n == 2: return b
        for _ in range(n - 2):
            c = a + b
            a = b
            b = c
        return c