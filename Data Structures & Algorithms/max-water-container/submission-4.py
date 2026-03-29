class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) -1
        ans = 0
        while l < r:
            cand = (min(heights[l], heights[r]) * (r - l)) 
            print(l, r, r - l, cand)
            ans = max(ans, cand)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

        return ans 