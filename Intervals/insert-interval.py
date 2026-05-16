class Solution:
    # # O(nlogn)
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     result = []
    #     intervals.append(newInterval)
    #     intervals.sort()
    #     prev = intervals[0]
    #     for i in range(1, len(intervals)):
    #         curr = intervals[i]
    #         currStart = curr[0]
    #         currEnd = curr[1]
    #         prevEnd = prev[1]
    #         if currStart > prevEnd:
    #             result.append(prev)
    #             prev = curr
    #         else:
    #             prev[1] = max(prevEnd, currEnd)
    #         if i == len(intervals)-1:
    #             result.append(prev)
    #     return result
    
    #O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        inserted = False

        while i < len(intervals):
            curr = intervals[i]

            # Current interval completely before new interval
            if curr[1] < newInterval[0]:
                res.append(curr)

            # Current interval completely after new interval
            elif curr[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)
                    inserted = True
                res.append(curr)

            # Overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[1] = max(newInterval[1], curr[1])

            i += 1

        if not inserted:
            res.append(newInterval)

        return res
    
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [2,3]
print(Solution().insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [6,8]
print(Solution().insert(intervals, newInterval))
