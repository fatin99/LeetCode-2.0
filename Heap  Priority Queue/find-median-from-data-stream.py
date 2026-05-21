import heapq


class MedianFinder:

    def __init__(self):
        self.size = 0
        # Space: O(n)
        self.maxHeap = []
        self.minHeap = []

    # Time: O(m∗logn)
    def addNum(self, num: int) -> None:
        if len(self.minHeap) > 0 and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)

        # Rebalance
        while len(self.minHeap) > len(self.maxHeap):
            prev = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, prev)
        while len(self.maxHeap) > len(self.minHeap) + 1:
            prev = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, prev)

        self.size += 1

    # Time: O(m)
    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return self.maxHeap[0]


# input_command = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# input_num = [[], [1], [2], [], [3], []]
# input_command = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# input_num = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
# input_command = ["MedianFinder","addNum","addNum","findMedian"]
# input_num = [[],[0],[0],[]]
input_command = [
    "MedianFinder",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
    "addNum",
    "findMedian",
]
input_num = [
    [],
    [6],
    [],
    [10],
    [],
    [2],
    [],
    [6],
    [],
    [5],
    [],
    [0],
    [],
    [6],
    [],
    [3],
    [],
    [1],
    [],
    [0],
    [],
    [0],
    [],
]
obj = None
for command, num in zip(input_command, input_num):
    if command == "MedianFinder":
        obj = MedianFinder()
    elif command == "addNum":
        obj.addNum(num[0])
    elif command == "findMedian":
        print(obj.findMedian())
