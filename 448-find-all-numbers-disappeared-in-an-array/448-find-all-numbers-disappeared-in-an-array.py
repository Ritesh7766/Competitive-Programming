class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            while nums[num - 1] != num:
                temp = nums[num - 1]
                nums[num - 1] = num
                num = temp
        
        res = []
        for i in range(len(nums) ):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
        