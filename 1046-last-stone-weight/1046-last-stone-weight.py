class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -1 * stone)
        
        weight = 0
        while heap:
            x = -1 * heapq.heappop(heap)
            if not heap: return x
            y = -1 * heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
            weight = x - y
        return weight
                