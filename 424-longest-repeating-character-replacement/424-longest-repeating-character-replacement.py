class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = collections.defaultdict(int)
        left, res = 0, 0
        
        for right in range(len(s)):
            mp[s[right]] += 1
            while ((right - left + 1) - max(mp.values()) ) > k:
                mp[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res