class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [0] * n, [0] * n
        
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        postfix[-1] = 1
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        return [prefix[i] * postfix[i] for i in range(n)]
        