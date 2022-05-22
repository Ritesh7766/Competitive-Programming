class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = collections.defaultdict(int)
        for i in range(len(s) - 9):
            mp[s[i : i + 10]] += 1
        return [key for key, value in mp.items() if value > 1]