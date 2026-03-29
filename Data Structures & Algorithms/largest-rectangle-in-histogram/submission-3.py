class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #ans = [0]
        def dfs(idxStart, idxCurr, smallest_height):
            if idxCurr == len(heights):
                return (idxCurr - idxStart) * smallest_height
            ret = max(
                (idxCurr - idxStart) * smallest_height,
                dfs(idxStart, idxCurr+1, min(smallest_height, heights[idxCurr])),
                dfs(idxCurr, idxCurr+1, heights[idxCurr])
            )
            return ret
        
        return dfs(0, 0, heights[0])
   #
  ##
  ## 
  ## #
# ####
######