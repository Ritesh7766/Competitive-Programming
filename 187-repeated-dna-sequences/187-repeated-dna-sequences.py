class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, exists = set(), set()
        
        for i in range(len(s) - 10 + 1):
            sequence = s[i : i + 10]
            if sequence in exists: res.add(sequence)
            else: exists.add(sequence)
        return res