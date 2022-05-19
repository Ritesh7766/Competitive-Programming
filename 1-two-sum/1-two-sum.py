class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        # If (target - current_num) exists in the map, than return (target-current_num, current_num).
        for i, num in enumerate(nums):
            required = target - num
            if required in mp: return [i, mp[required]]
            mp[num] = i
        
        return None