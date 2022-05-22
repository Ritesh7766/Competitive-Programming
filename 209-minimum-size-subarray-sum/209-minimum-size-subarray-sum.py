from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, mn_ln = 0, inf
        sm = 0
        
        for r in range(len(nums)):
            sm += nums[r]
            while sm >= target:
                mn_ln = min(mn_ln, r - l + 1)
                sm -= nums[l]
                l += 1
        return mn_ln if mn_ln != inf else 0
            
            
        
        