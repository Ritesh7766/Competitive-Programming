class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        # Find all anagrams of p in s.
        key, mp = [0] * 26, [0] * 26
        matches = 0
        
        for ch in p:
            key[ord(ch) - ord('a')] += 1
        
        for i in range(len(p)):
            mp[ord(s[i]) - ord('a')] += 1
            
        for i in range(26):
            if mp[i] == key[i]:
                matches += 1

        l, res = 0, []
        for r in range(len(p), len(s)):
            if matches == 26:
                res.append(l)
            matches = 0
            mp[ord(s[l]) - ord('a')] -= 1
            mp[ord(s[r]) - ord('a')] += 1
            for i in range(26):
                if mp[i] == key[i]:
                    matches += 1
            l += 1
            
        if matches == 26:
            res.append(l)
        return res