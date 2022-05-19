class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The number of characters grouped by alphabets will serve as a key to
        # identify a set of anagrams.
        
        mp = collections.defaultdict(list)
        for str in strs:
            key = [0] * 26
            for ch in str: key[ord(ch) - ord('a')] += 1
            mp[tuple(key)].append(str)
        
        return [group_anagram for _, group_anagram in mp.items()]