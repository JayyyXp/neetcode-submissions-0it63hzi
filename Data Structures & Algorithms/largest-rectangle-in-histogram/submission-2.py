class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = [0]
        def dfs(idxStart, idxCurr, smallest_height):
            if idxCurr == len(heights):
                ans[0] = max(
                    (idxCurr - idxStart) * smallest_height,
                    ans[0]
                )
                return
            print(idxStart, idxCurr, smallest_height, (idxCurr - idxStart) * smallest_height)
            ans[0] = max(
                (idxCurr - idxStart) * smallest_height,
                ans[0]
            )
            dfs(idxStart, idxCurr+1, min(smallest_height, heights[idxCurr]))
            dfs(idxCurr, idxCurr+1, heights[idxCurr])

        dfs(0, 0, heights[0])
        return ans[0]
   #
  ##
  ## 
  ## #
# ####
######