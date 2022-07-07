class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        v1, v2 = [0] * 26, [0] * 26
        s1, s2 = [0] * 26, [0] * 26
        for ch in word1: 
            v1[ord(ch) - ord('a')] += 1
            s1[ord(ch) - ord('a')] = 1
        for ch in word2: 
            v2[ord(ch) - ord('a')] += 1
            s2[ord(ch) - ord('a')] = 1
        v1.sort()
        v2.sort()
        return v1 == v2 and s1 == s2