class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            required = target - num
            if required in mp:
                return [mp[required], i]
            mp[num] = i
        return None