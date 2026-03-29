class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [-1000]
        memo = {}
        def helper(s, e):
            if s == e:
                return
            if (s, e) in memo:
                return
            else:
                temp = sum(nums[s:e])
                memo[(s,e)] = temp
                ans[0] = max(ans[0], temp)
                helper(s+1, e)
                helper(s, e-1)
                #helper(s+1, e-1)


        helper(0, len(nums))

        return ans[0]