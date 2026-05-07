import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone_y = heapq.heappop_max(stones)
            stone_x = heapq.heappop_max(stones)
            if stone_x != stone_y:
                remaining_stone = abs(stone_x - stone_y)
                heapq.heappush_max(stones, remaining_stone)
        if not stones:
            return 0
        else:
            return stones[0]


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
