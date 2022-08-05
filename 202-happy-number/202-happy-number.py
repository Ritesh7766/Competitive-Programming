class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while n != 1:
            tmp = 0
            while n > 0:
                tmp += ((n % 10) ** 2)
                n //= 10
            if tmp in seen: return False
            seen.add(tmp)
            n = tmp
        return True