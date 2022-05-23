class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_unique, exists = 0, set()
        for ch in s:
            if ch not in exists: max_unique += 1
            exists.add(ch)
            
        '''
        Subproblem: Find all the substring with exactly
        v unique characters such that the frequency of 
        each character is at least k.
        
        If the number of unique characters in the window
        is <= curr_unique, then expand the window.
        Else reduce its size.
        
        If frequency of each unique character in the 
        window is at least k, then record its length.
        '''
        max_ln = 0
        for curr_unique in range(1, max_unique + 1):
            char_mp, l = defaultdict(int), 0
            for r in range(len(s)):
                char_mp[ord(s[r]) - ord('a')] += 1 
                # Reduce the window size.
                while len(char_mp) > curr_unique:
                    ind = ord(s[l]) - ord('a')
                    char_mp[ind] -= 1
                    if char_mp[ind] == 0:
                        del char_mp[ind]
                    l += 1
                if min(char_mp.values()) >= k:
                    max_ln = max(max_ln, r - l + 1)
        return max_ln
                    
                    