class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mn_sm = sum(cardPoints[0 : len(cardPoints) - k])
        sm, left = mn_sm, 0
        for right in range(len(cardPoints) - k, len(cardPoints) ):
            sm -= cardPoints[left]
            sm += cardPoints[right]
            mn_sm = min(mn_sm, sm)
            left += 1
        return sum(cardPoints) - mn_sm
            