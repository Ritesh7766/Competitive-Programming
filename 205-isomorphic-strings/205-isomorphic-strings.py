class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mp1, mp2 = {}, {}
        
        for i in range(len(s) ):
            if s[i] in mp1 and mp1[s[i]] != t[i]:
                return False
            mp1[s[i]] = t[i]
            if t[i] in mp2 and mp2[t[i]] != s[i]:
                return False
            mp2[t[i]] = s[i]
        return True