class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Precompute the cumulative product excluding the current element [Lets call this prefix.
        # Do the same with nums.reverse [Lets call this postfix].
        # For each element return prefix * postfix for that element.
        
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        return [prefix[i] * postfix[i] for i in range(n)]