class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        exists = {}
        
        for i, num in enumerate(nums):
            if num in exists and abs(exists[num] - i) <= k:
                return True
            exists[num] = i
        return False