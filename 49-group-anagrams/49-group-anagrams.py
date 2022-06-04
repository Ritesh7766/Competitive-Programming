class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        
        for str in strs:
            key = [0] * 26
            for ch in str:
                key[ord(ch) - ord('a')] += 1
            mp[tuple(key)].append(str)
            
        return [group for _, group in mp.items()]