from math import inf

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp, mn = {}, inf
        for i, card in enumerate(cards):
            if card in mp:
                mn = min(mn, i - mp[card] + 1)
                mp[card] = i
            else: mp[card] = i
                
        return mn if mn != inf else -1