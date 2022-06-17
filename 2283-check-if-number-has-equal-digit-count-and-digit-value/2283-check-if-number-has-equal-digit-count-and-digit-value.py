class Solution:
    def digitCount(self, num: str) -> bool:
        mp = collections.defaultdict(int)
        
        for dig in num:
            mp[int(dig)] += 1

        for i in range(len(num) ):
            if mp[i] != int(num[i]):
                return False
        return True