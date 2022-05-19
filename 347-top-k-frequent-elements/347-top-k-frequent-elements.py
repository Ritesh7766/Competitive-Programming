class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort but instead of using the elements of the list as key
        # we use the count of each element as key.
        # An element of going to exists at most array.length times.
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        mp = collections.defaultdict(int)
        
        for num in nums:
            mp[num] += 1
            
        for num, cnt in mp.items():
            buckets[cnt].append(num)
            
        res = []
        for i in range(n, -1, -1):
            if k == 0: break
            k -= len(buckets[i])
            for num in buckets[i]: res.append(num)
        return res