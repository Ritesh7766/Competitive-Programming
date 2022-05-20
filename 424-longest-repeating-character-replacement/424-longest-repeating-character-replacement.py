class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = [0] * 26
        left = 0
        
        mx_ln = 0
        for right in range(len(s)):
            mp[ord(s[right]) - ord('A')] += 1
            if ((right - left + 1) - max(mp)) <= k:
                mx_ln = max(mx_ln, right - left + 1)
            else: 
                mp[ord(s[left]) - ord('A')] -= 1
                left += 1
                
        return mx_ln
            