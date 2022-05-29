class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        mx_left, mx_right = [0] * n, [0] * n
        
        mx_left[0] = height[0]
        for i in range(1, n):
            mx_left[i] = max(height[i], mx_left[i - 1])
        
        mx_right[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            mx_right[i] = max(height[i], mx_right[i + 1])
        
        total = 0
        for i in range(n):
            amt = (min(mx_left[i], mx_right[i]) - height[i])
            if amt > 0: total += amt
        return total