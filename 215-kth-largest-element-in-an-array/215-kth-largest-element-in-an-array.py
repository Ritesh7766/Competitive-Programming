from random import randrange

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Arrays are 0-indexed.
        k -= 1
        
        def partition(left, right):
            if left == right: return left
            pivot = randrange(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            i = left - 1
            for j in range(left, right):
                if nums[j] >= nums[right]:
                    i += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            return i + 1
        
        left, right = 0, len(nums) - 1
        position = partition(left, right)
        while position != k:
            if position < k:
                left = position + 1
            elif position > k:
                right = position - 1
            position = partition(left, right)
        return nums[position]