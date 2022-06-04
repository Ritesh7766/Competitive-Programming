class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        mp = collections.defaultdict(int)
        
        for i in range(len(s)):
            mp[ord(s[i]) - ord('a')] += 1
            mp[ord(t[i]) - ord('a')] -= 1
            
        for _, count in mp.items():
            if count != 0: return False
        return True