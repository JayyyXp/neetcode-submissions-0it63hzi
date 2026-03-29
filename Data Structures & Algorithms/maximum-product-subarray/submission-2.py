class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        #def dfs(i):
        #    if i == len(nums):
        #        return 1
        #    ret = max(
        #        dfs(i+1) * nums[i], # include i'th number
        #        dfs(i+1)            # don't include
        #    )
        #    print(i, ret)
        #    return ret
        #return dfs(0)

        ans = [-float('inf')]

        for s in range(len(nums)):
            for e in range(s,len(nums)):
                c = 1
                for i in range(s,e+1):
                    print(c*nums[i])
                    c = c*nums[i]
                print(list(range(s,e+1)), c)
                ans[0] = max(ans[0], c)

        return ans[0]