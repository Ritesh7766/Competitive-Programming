class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left, sm = 0, 0
        subarrays = 0
        for right in range(len(nums) ):
            sm += nums[right]
            while sm * (right - left + 1) >= k:
                sm -= nums[left]
                left += 1
            subarrays += (right - left + 1)
        return subarrays