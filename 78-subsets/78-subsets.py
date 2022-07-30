class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(elm = 0, sub_set = [], power_set = []):
            if elm == len(nums):
                return power_set + [sub_set]
            
            power_set = sub(elm + 1, sub_set, power_set)
            power_set = sub(elm + 1, sub_set + [nums[elm]], power_set)
            return power_set
        
        return sub()