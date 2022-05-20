class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        mp1, mp2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            mp1[ord(s1[i]) - ord('a')] += 1
            mp2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if mp1[i] == mp2[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            mp2[index] += 1
            if mp1[index] == mp2[index]: matches += 1
            elif mp1[index] + 1 == mp2[index]: matches -= 1
            
            index = ord(s2[l]) - ord('a')
            mp2[index] -= 1
            if mp1[index] == mp2[index]: matches += 1
            elif mp1[index] - 1 == mp2[index]: matches -= 1
            l += 1
        return matches == 26
            