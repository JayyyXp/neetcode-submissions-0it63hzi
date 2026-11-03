class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        added = False
        for a, b in intervals:
            if ans and ans[-1][1] >= a:
                ans[-1][1] = max(ans[-1][1], b)
                continue
            # CURR: |----|
            # CAND:        |----| 
            if b < newInterval[0]:
                ans.append([a,b])
                continue

            # CURR:        |----|
            # CAND: |----| 
            if newInterval[1] < a:
                if not added:
                    added = True
                    ans.append(newInterval)
                ans.append([a,b])
                continue

            # CURR: |----|
            # CAND:    |----| 
            #
            # CURR: |----|
            # CAND:  |--| 
            if newInterval[0] <= b:
                added = True
                ans.append([min(a, newInterval[0]), max(b, newInterval[1])])
        if not added:
            ans.append(newInterval)
        return ans