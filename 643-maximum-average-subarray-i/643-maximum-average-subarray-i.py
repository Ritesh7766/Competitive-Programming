class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, sm = 0, 0
        for i in range(k):
            sm += nums[i]
        
        mx_avg = sm / k
        for right in range(k, len(nums)):
            sm += (nums[right] - nums[left])
            mx_avg = max(mx_avg, sm / k)
            left += 1
        return mx_avg