class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans = -float('inf')
        for i in range(len(nums)):
            helper = 0
            for j in range(i, i+len(nums)):
                #print(i, nums[j%len(nums)],helper)
                helper += nums[j%len(nums)]
                ans = max(ans,helper)
        return ans 