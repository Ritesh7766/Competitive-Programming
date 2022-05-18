class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        mx_len = 0
        for num in nums:
            if (num - 1) in nums: continue
            ln = 1
            while (num + ln) in nums: ln += 1
            mx_len = max(mx_len, ln)
        
        return mx_len