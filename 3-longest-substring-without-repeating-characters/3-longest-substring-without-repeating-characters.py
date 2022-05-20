class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, char_set = 0, set()
        
        mx_ln = 0
        for right in range(len(s)):
            while s[right] in char_set: 
                char_set.remove(s[left])
                left += 1
            mx_ln = max(mx_ln, right - left + 1)
            char_set.add(s[right])
        return mx_ln