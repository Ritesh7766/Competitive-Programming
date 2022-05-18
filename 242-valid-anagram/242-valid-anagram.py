class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If two string have exactly the same number of characters of each type, than they are anagrams.
        if len(s) != len(t): return False
        mp = collections.defaultdict(int)
        
        for i in range(len(s)):
            mp[s[i]] += 1
            mp[t[i]] -= 1
        
        for ch, cnt in mp.items():
            if cnt != 0: return False
        
        return True