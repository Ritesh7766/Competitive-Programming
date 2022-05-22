class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp, l = set(), 0
        mx_ln = 0
        for r in range(len(s)):
            while s[r] in mp:
                mp.remove(s[l])
                l += 1
            mp.add(s[r])
            mx_ln = max(mx_ln, len(mp))
        return mx_ln
            