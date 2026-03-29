class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        #intervals.sort()
        ans = [-1]*len(queries)

        for i, q in enumerate(queries):
            cand = float('inf')
            qIdx = -1
            for j, (intStart, intEnd) in enumerate(intervals):
                if intStart <= q <= intEnd:
                    if intEnd - intStart + 1 < cand:
                        cand = intEnd - intStart + 1
                        qIdx = j
            if cand < float('inf'):
                ans[i] = cand
        return ans