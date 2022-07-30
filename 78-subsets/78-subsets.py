class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Recursive solution
        def sub(elm = 0, sub_set = [], power_set = []):
            if elm == len(nums):
                return power_set + [sub_set]
            
            power_set = sub(elm + 1, sub_set, power_set)
            power_set = sub(elm + 1, sub_set + [nums[elm]], power_set)
            return power_set
        return sub()
        '''
        power_set, n = [], len(nums)
        for i in range(2 ** n):
            sub_set = []
            for k in range(n):
                if i & (1 << k):
                    sub_set.append(nums[k])
            power_set.append(sub_set)
        return power_set