class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        left, right = 0, n - 1
        
        cur = n - 1
        while left <= right:
            n1, n2 = nums[left] ** 2, nums[right] ** 2
            if n1 >= n2:
                arr[cur] = n1
                left += 1
            else:
                arr[cur] = n2
                right -= 1
            cur -= 1
        return arr