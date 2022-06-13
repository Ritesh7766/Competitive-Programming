class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        res = []
        for k, v in freq.items():
            if v == 1: res.append(k)
        return res