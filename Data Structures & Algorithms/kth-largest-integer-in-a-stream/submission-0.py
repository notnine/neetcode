import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        self.n = len(self.heap) if self.heap else 0
        while self.n > k:
            heapq.heappop(self.heap)
            self.n -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.n += 1
        if self.n > self.k:
            heapq.heappop(self.heap)
            self.n -= 1

        return self.heap[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)