class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        for i, h in enumerate(height):
            maxL = max(height[:i]) if i > 0 else 0
            maxR = max(height[i+1:]) if i < len(height) - 1 else 0
            ans += max(min(maxL, maxR) - h, 0)
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