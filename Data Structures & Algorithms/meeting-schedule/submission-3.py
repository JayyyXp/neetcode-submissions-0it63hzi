"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        for int1, int2 in zip(intervals[:-1], intervals[1:]):
            print("loop")
            if int1.end > int2.start:
                return False
        return True