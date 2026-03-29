class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #ans = [0]
        cache = {}
        def dfs(idxStart, idxCurr, smallest_height):
            if idxCurr == len(heights):
                return (idxCurr - idxStart) * smallest_height
            if (idxStart, idxCurr) in cache:
                return cache[(idxStart, idxCurr)]
            ret = max(
                (idxCurr - idxStart) * smallest_height,
                dfs(idxStart, idxCurr+1, min(smallest_height, heights[idxCurr])),
                dfs(idxCurr, idxCurr+1, heights[idxCurr])
            )
            cache[(idxStart, idxCurr)] = ret
            return ret
        
        return dfs(0, 0, heights[0])
   #
  ##
  ## 
  ## #
# ####
######