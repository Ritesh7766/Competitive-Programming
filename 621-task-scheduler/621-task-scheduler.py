class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = collections.deque()
        mp = collections.defaultdict(int)
        
        for task in tasks:
            mp[task] += 1
        
        for _, cnt in mp.items():
            heapq.heappush(heap, -1 * cnt)
        
        time = 0
        while heap or queue:
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1
                if cnt != 0:
                    queue.append((cnt, time + n))
            if queue and queue[0][1] == time:
                cnt, _ = queue.popleft()
                heapq.heappush(heap, cnt)
            time += 1
        return time