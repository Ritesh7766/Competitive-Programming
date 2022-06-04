class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        mp = collections.defaultdict(int)
        
        for num in nums: mp[num] += 1
        
        for num, count in mp.items():
            bucket[count].append(num)
            
        res = []
        for i in range(len(nums), -1, -1):
            if k == 0: break
            k -= len(bucket[i])
            for num in bucket[i]: res.append(num)
        return res