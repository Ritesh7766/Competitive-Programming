class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        good_pairs = 0
        for num, frq in freq.items():
            good_pairs += (frq * (frq - 1)) // 2
        return good_pairs