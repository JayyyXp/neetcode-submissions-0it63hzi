class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        i = 0

        # CURR: |----|
        # CAND:        |----| 
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i][:])
            i += 1

        # CURR: |----|
        # CAND:   |----|
        toAdd = newInterval[:]
        while i < len(intervals) and intervals[i][0] <= toAdd[1]:
            toAdd = [
                min(toAdd[0], intervals[i][0]),
                max(toAdd[1], intervals[i][1])
            ]       
            i += 1
        ans.append(toAdd)

        ans.extend(intervals[i:])
        return ans 