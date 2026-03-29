class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        glbMax = nums[0]
        for n in nums:
            curMax = max(n, curMax+n)
            glbMax = max(glbMax, curMax)
        return glbMax 