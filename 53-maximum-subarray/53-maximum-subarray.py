class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_sum, sm = nums[0], nums[0]
        for i in range(1, len(nums)):
            sm = max(sm + nums[i], nums[i])
            mx_sum = max(mx_sum, sm)
        return mx_sum