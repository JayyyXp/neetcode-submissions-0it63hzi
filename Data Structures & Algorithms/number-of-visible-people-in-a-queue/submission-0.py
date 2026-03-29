class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = []

        for i in range(len(heights)-1):
            maxH = heights[i+1]
            res = 1
            for j in range(i+2,len(heights)):
                if min(heights[i], heights[j]) > maxH:
                    res += 1
                maxH = max(maxH, heights[j])
            ans.append(res)
        ans.append(0)
        return ans 
