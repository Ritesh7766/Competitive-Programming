class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a map
        mp = {}
        
        for i, num in enumerate(nums):
            # Check if the required number exists in the map.
            required = target - num
            # If it exists in the map, than we have found the unique solution.
            if required in mp: return [i, mp[required]]
            # Otherwise map the num to its index.
            mp[num] = i
            
        return None # This line will probably never get executed because solution is guranteed to exist. 