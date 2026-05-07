class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if currStart < prevEnd:
                count += 1
            else:
                prevEnd = currEnd

        return count
