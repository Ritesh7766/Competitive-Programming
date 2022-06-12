class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, l = collections.deque(), 1
        
        res = []
        for r in range(k):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
        res.append(nums[q[0]])
        for r in range(k, len(nums) ):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            res.append(nums[q[0]])
            l += 1
        return res