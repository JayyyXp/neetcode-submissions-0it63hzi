class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        def checker(sign):
            ans = 1
            l = 0
            for r in range(1, len(nums)):
                if sign(nums[r], nums[r-1]):
                    ans = max(ans, r - l + 1)
                else:
                    l = r
            return ans
            
        return max(
            checker(lambda x, y: x > y),
            checker(lambda x, y: x < y)
        )