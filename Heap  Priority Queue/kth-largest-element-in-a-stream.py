import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num_heap = nums
        self.k = k
        heapq.heapify(self.num_heap)
        while len(self.num_heap) > k:
            heapq.heappop(self.num_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.num_heap, val)
        while len(self.num_heap) > self.k:
            heapq.heappop(self.num_heap)
        if len(self.num_heap) > 0:
            return self.num_heap[0]
        else:
            return None


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
heap = KthLargest(1, [])
print(heap.add(-3))
print(heap.add(-2))
print(heap.add(-4))
print(heap.add(0))
print(heap.add(4))
