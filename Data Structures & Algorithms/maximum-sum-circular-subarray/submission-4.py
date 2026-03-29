class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        glbMax = nums[0]
        curMin = 0
        glbMin = nums[0]
        total = 0
        for n in nums:
            curMax = max(n, curMax + n)
            glbMax = max(glbMax, curMax)
            curMin = min(n, curMin + n)
            glbMin = min(glbMin, curMin)
            total += n
        return max(glbMax, total - glbMin) if glbMax > 0 else glbMax