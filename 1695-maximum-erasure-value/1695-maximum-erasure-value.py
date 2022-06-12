class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum, sm = 0, 0
        
        l, hash_set = 0, set()
        for r in range(len(nums) ):
            while nums[r] in hash_set:
                hash_set.remove(nums[l])
                sm -= nums[l]
                l += 1
            hash_set.add(nums[r])
            sm += nums[r]
            max_sum = max(max_sum, sm)
        return max_sum