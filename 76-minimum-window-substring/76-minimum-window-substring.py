from math import inf

class Solution:
    def minWindow(self, s: str, t: str) -> str:     
        key = Counter(t)
        max_unique = len(key)
        mp = collections.defaultdict(int)
        
        l, found = 0, 0
        res = (inf, 0, 0)
        for r in range(len(s)):
            mp[s[r]] += 1
            if s[r] in key and mp[s[r]] == key[s[r]]:
                found += 1
            while found == max_unique:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                mp[s[l]] -= 1
                if s[l] in key and mp[s[l]] < key[s[l]]:
                    found -= 1
                l += 1
        return '' if res[0] is inf else s[res[1] : res[2] + 1]