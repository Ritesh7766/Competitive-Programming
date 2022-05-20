class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = [0] * 26
        
        for ch in s1: mp1[ord(ch) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            mp2 = [0] * 26
            for ch in s2[i : i + len(s1)]: mp2[ord(ch) - ord('a')] += 1
            if tuple(mp1) == tuple(mp2): return True
        return False