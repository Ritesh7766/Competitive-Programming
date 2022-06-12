from math import inf

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hash_set, l = set(), 0
        
        mn = inf
        for r in range(len(cards) ):
            while cards[r] in hash_set:
                mn = min(r - l + 1, mn)
                hash_set.remove(cards[l])
                l += 1
            hash_set.add(cards[r])
        return -1 if mn is inf else mn