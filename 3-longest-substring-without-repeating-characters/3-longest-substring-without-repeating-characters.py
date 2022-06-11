class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, n = 0, len(s)
        exists, mx_len = set(), 0
        
        for right in range(n):
            while left <= right and s[right] in exists:
                exists.remove(s[left])
                left += 1
            exists.add(s[right])
            mx_len = max(mx_len, right - left + 1)
        
        return mx_len