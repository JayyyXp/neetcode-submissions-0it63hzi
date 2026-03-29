class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(nums, prev):
            if len(nums) == 0:
                return 0


            ans = 0
            for i, num in enumerate(nums):
                if num > prev:
                    ans = max(helper(nums[i:], num) +1, ans)
                #else:
                #    ans = max(helper(nums[i:], num), ans)
            return ans

        return helper(nums, -1001)
