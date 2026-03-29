class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ans = [0]
        memo = {}
        def dfs(idx, curr):
            if idx == len(nums):
                return curr == target
            
            return (
                dfs(idx + 1, curr + nums[idx]) +
                dfs(idx + 1, curr - nums[idx])
            )
        
        return dfs(0, 0)


        


