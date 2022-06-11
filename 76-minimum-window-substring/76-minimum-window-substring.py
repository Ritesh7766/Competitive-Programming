from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        key = Counter(t)
        max_unique = len(key)
        mp = collections.defaultdict(int)
        
        left, found = 0, 0
        res = (inf, 0, 0)
        for right in range(len(s) ):
            mp[s[right]] += 1
            if s[right] in key and mp[s[right]] == key[s[right]]:
                found += 1
            while found == max_unique:
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right + 1)
                if s[left] in key and mp[s[left]] == key[s[left]]:
                    found -= 1
                mp[s[left]] -= 1
                left += 1
        return '' if res[0] is inf else s[res[1] : res[2]]