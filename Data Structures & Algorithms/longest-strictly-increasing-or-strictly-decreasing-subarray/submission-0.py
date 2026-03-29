class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        l = 0 
        prev = -float('inf')
        for r in range(len(nums)):
            if nums[r] > prev:
                ans = max(ans, r - l + 1)
            else:
                l = r
            prev = nums[r]
                
        l = 0 
        prev = float('inf')
        for r in range(len(nums)):
            if nums[r] < prev:
                ans = max(ans, r - l + 1)
            else:
                l = r
            prev = nums[r]
        
        return ans