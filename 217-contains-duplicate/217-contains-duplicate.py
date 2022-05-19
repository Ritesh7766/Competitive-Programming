class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize a hash-set
        exists = set()
        
        for num in nums:
            # If the number already exists in the hash-set return True.
            if num in exists: return True
            # Otherwise add it to the hash set.
            exists.add(num)
        
        # If no duplicates exists return False.
        return False