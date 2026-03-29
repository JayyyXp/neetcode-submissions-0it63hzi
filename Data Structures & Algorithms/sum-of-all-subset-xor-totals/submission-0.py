class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        from functools import reduce

        ans =  [0]
        helper = [0]
        def dfs(i):
            if i == len(nums):
                ans[0] += reduce(lambda x, y: x^y, helper)
                return
            
    
            helper.append(nums[i])
            dfs(i+1) 
            helper.pop()
            dfs(i+1) 

        dfs(0)
        return ans[0]