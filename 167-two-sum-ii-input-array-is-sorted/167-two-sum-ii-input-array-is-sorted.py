class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        
        while left < right:
            sm = numbers[left] + numbers[right]
            if sm == target:
                return [left + 1, right + 1]
            left, right = (left, right - 1) if sm > target else (left + 1, right)
        
        return None