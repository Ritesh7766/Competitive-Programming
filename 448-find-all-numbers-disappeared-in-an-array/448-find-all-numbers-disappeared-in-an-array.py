class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        u = set([i for i in range(1, len(nums) + 1)])
        s = set([i for i in nums])
        
        return u - s