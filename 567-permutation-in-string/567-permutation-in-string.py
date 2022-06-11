class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        key, mp = [0] * 26, [0] * 26
        
        for ch in s1:
            key[ord(ch) - ord('a')] += 1
        
        for i in range(len(s1) ):
            mp[ord(s2[i]) - ord('a')] += 1
            
        left = 0
        for right in range(len(s1), len(s2) ):
            if tuple(mp) == tuple(key): return True
            mp[ord(s2[right]) - ord('a')] += 1
            mp[ord(s2[left]) - ord('a')] -= 1
            left += 1
        return tuple(mp) == tuple(key)
        