class Solution:
    def minWindow(self, s: str, t: str) -> str:
        key = Counter(t)
        mp = collections.defaultdict(int)
        max_found = len(key)
        
        l, found = 0, 0
        res = (inf, 0, 0)
        for r in range(len(s) ):
            mp[s[r]] += 1
            if s[r] in key and mp[s[r]] == key[s[r]]:
                found += 1
            while found == max_found:
                if res[0] > (r - l + 1):
                    res = (r - l + 1, l, r)
                if s[l] in key and mp[s[l]] == key[s[l]]:
                    found -= 1
                mp[s[l]] -= 1
                l += 1
                
        return '' if res[0] is inf else s[res[1] : res[2] + 1]