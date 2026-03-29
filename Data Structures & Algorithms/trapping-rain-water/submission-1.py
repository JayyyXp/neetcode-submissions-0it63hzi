class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        n = len(height)
        for i in range(n):
            maxL = max(height[:i]) if i > 0 else 0
            maxR = max(height[i+1:]) if i < n - 1 else 0
            trapped = min(maxL, maxR) - height[i]
            if trapped > 0:
                ans += trapped
        return ans
        #r, l = 1, 0
        #ans = 0
        #while r < len(height):
        #    if height[r] >= height[l]:
        #        h = min(height[r], height[l])
        #        if h > 0:
        #            for i in range(l + 1, r):
        #                ans += h - height[i]
        #            print(l,r, h, ans)
        #        l = r       
        #    r += 1
        return ans