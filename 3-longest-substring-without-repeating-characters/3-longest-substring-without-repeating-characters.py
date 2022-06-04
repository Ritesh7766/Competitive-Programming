class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exists = set()
        
        left, mx_len = 0, 0
        for right in range(len(s)):
            while s[right] in exists:
                exists.remove(s[left])
                left += 1
            mx_len = max(mx_len, right - left + 1)
            exists.add(s[right])
        return mx_len