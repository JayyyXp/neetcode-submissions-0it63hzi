class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if end > intervals[i][0]:
                if end > intervals[i][1]:
                    end = intervals[i][1]
                ans += 1
            else:
                end = intervals[i][1]
        return ans#[0]