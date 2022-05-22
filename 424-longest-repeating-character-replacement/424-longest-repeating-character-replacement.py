class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp, l = [0] * 26, 0
        mx_ln = 0
        for r in range(len(s)):
            mp[ord(s[r]) - ord('A')] += 1
            while ((r - l + 1) - max(mp)) > k:
                mp[ord(s[l]) - ord('A')] -= 1
                l += 1
            mx_ln = max(mx_ln, r - l + 1)
        return mx_ln
        