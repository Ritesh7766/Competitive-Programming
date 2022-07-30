class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n, mp = 0, {}
        for i, ch in enumerate(s):
            if ch.isalpha():
                mp[n] = (ch, i)
                n += 1
                
        res = []
        for i in range(2 ** n):
            wrd = [ch for ch in s]
            for k in range(n):
                if i & (1 << k):
                    wrd[mp[k][1]] = mp[k][0].upper() if mp[k][0].islower() else mp[k][0].lower()
            res.append(''.join(wrd) )
        return res