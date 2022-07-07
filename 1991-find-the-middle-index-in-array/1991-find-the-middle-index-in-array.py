class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        for i in range(n):
            leftsum = nums[i - 1] if i > 0 else 0
            rightsum = nums[n - 1] - nums[i]
            if leftsum == rightsum:
                return i
        
        return -1