class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        cnt = 0
        for i in range(0, len(s), 2):
            cnt += len([ch for ch in s[i] if ch == '*'])
        return cnt