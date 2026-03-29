class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        ans = []
        # Pacific, Atlantic
        flow = [False, False]
        seen = set()
        def canFlow(i,j, prevValue): 
            # canFlow Pacific
            if i == -1 or j == -1:
                flow[0] = True
                return
            # canFlow Atlantic
            if i == (ROWS) or j == (COLS):
                flow[1] = True
                return
            if (i,j) in seen:
                return
            if heights[i][j] > prevValue:
                return
            seen.add((i,j))
            canFlow(i+1,j, heights[i][j]) 
            canFlow(i-1,j, heights[i][j]) 
            canFlow(i,j+1, heights[i][j]) 
            canFlow(i,j-1, heights[i][j]) 


        for i in range(ROWS):
            for j in range(COLS):
                flow = [False, False]
                seen = set()
                canFlow(i,j, float('inf'))
                if all(flow):
                    ans.append([i,j])

        return ans