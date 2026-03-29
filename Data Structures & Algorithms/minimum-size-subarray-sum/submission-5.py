class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0,0
        currSum = 0
        ans = len(nums) 
        total = 0
        while r < len(nums):
            currSum += nums[r]
            total += nums[r]
            r += 1
            while currSum >= target:
                ans = min(ans, r-l)
                currSum -= nums[l]
                l += 1

        return 0 if total < target else ans
