class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        def max_subarray(l = 0, u = len(nums) - 1):
            if l == u: return 0
            elif (u - l) == 1: return max(nums[u] - nums[l], 0)
            mid = (l + u) // 2
            m1 = max_subarray(l, mid)
            m2 = max_subarray(mid + 1, u)
            return max(m1, m2, max(nums[mid + 1:u + 1]) - min(nums[l:mid + 1]) )
        
        return max_subarray()
            