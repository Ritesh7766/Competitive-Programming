class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums, visited = Counter(nums), set()
        
        def dfs(u, res):
            visited.add(u)
            if (u - 1) not in nums and (u + 1) not in nums and nums[u] == 1:
                res.append(u)
            for v in [u - 1, u + 1]:
                if v in nums and v not in visited:
                    res = dfs(v, res)
            return res
        
        res = []
        for num in nums:
            res = dfs(num, res)
        return res