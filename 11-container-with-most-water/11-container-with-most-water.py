class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        
        mx_area = 0
        while left < right:
            mx_area = max(mx_area, min(height[left], height[right]) * (right - left))
            left, right = (left + 1, right) if height[left] <= height[right] else (left, right - 1)
        return mx_area