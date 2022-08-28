class Solution:
    def removeStars(self, s: str) -> str:
        stack = collections.deque()
        
        for ch in s:
            if ch == '*': stack.popleft()
            else: stack.appendleft(ch)
        
        res = ''
        while stack:
            res += stack.pop()
        return res