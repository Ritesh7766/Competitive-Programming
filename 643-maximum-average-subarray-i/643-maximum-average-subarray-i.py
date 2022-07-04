class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, sm = 0, 0
        for i in range(k):
            sm += nums[i]
        
        mx_sm = sm
        for right in range(k, len(nums)):
            sm += (nums[right] - nums[left])
            mx_sm = max(mx_sm, sm)
            left += 1
        return mx_sm / k