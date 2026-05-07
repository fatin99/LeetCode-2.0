class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        prev = intervals[0]
        for i in range(len(intervals)):
            currStart = intervals[i][0]
            prevEnd = prev[1]
            if currStart > prevEnd:
                result.append(prev)
                prev = intervals[i]
            else:
                currEnd = intervals[i][1]
                prev[1] = max(prevEnd, currEnd)
            if i == len(intervals) - 1:
                result.append(prev)
        return result
