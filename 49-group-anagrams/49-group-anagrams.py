class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The number of characters grouped by alphabets is going to
        # serve as a key to identify anagrams.
        mp = collections.defaultdict(list)
        
        for str in strs:
            key = [0] * 26
            for ch in str: key[ord(ch) - ord('a')] += 1
            # Recall, lists are unhashable in python.
            mp[tuple(key)].append(str)
        
        res = []
        for key, group_anagrams in mp.items():
            res.append(group_anagrams)
        return res
        