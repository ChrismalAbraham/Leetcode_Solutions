class KthLargest:
    

    def __init__(self, k: int, nums: list):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num) -> int:
        heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)