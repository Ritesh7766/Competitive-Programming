class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        heap, cnt = [], collections.defaultdict(int)
        for x, y in roads:
            cnt[x] += 1
            cnt[y] += 1
            
        for city, conns in cnt.items():
            heapq.heappush(heap, (-1 * conns, city) )
            
        mx_imp = 0
        for i in range(n, 0, -1):
            if not heap: break
            conns, city = heapq.heappop(heap)
            mx_imp += i * conns * (-1)
        return mx_imp
        