class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(startIdx, prev):
            if startIdx == len(nums):
                return 0


            ans = 0
            for i in range(startIdx, len(nums)):
                num = nums[i]
                if num > prev:
                    if (i, num) in memo:
                        ans = max(memo[(i, num)] + 1, ans)
                    else:
                        temp = helper(i, num)
                        memo[(i, num)] = temp
                        ans = max(temp +1, ans)
                #else:
                #    ans = max(helper(nums[i:], num), ans)
            return ans

        return helper(0, -1001)
