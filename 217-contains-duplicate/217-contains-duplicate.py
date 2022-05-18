class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a hash-set
        exists = set()
        
        for num in nums:
            # if num already exists in the set return true.
            if num in exists: return True
            # Otherwise add it to the hash-set.
            exists.add(num)
        
        return False