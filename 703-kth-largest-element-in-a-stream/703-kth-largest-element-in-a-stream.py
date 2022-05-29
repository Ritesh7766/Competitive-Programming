class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kheap = []
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.kheap) < self.k:
            heapq.heappush(self.kheap, val)
        elif val > self.kheap[0]:
            tmp = heapq.heappop(self.kheap)
            heapq.heappush(self.kheap, val)
            heapq.heappush(self.heap, tmp)
        else: heapq.heappush(self.heap, val)
        return self.kheap[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)