class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        mx_ln = 0
        for num in nums:
            if (num - 1) not in nums:
                ln = 1
                while (num + ln) in nums: ln += 1
                mx_ln = max(mx_ln, ln)
        return mx_ln