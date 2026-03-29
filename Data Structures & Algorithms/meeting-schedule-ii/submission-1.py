"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        ints = sorted(intervals, key=lambda x: x.start)
        print(ints)
        scheduled = set()
        days = 0
        while True:
            maxTime = -1
            for i, interval in enumerate(ints):
                if i in scheduled:
                    continue
                if interval.start >= maxTime:
                    scheduled.add(i)
                    maxTime = interval.end

            days += 1
            if len(scheduled) == len(intervals):
                return days
