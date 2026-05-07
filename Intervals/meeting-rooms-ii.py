import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            earliestEnd = rooms[0]
            currEnd = intervals[i][1]
            if currStart < earliestEnd:
                heapq.heappush(rooms, currEnd)
            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, currEnd)
        return len(rooms)
