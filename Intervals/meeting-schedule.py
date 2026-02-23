class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def interval_lt(self, other):
    if not isinstance(other, Interval):
        return NotImplemented
    return self.start < other.start

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        Interval.__lt__ = interval_lt
        intervals.sort() 
        #Alternatively without interval_lt
        # intervals.sort(key=lambda i: i.start)
        for i in range(0, len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True

a = Interval(0,30)
b = Interval(5,10)
c = Interval(15,20)
print(Solution().canAttendMeetings([a, b, c]))