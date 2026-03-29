class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0
            if idx in cache:
                return cache[idx]
            ret = max(
                dfs(idx+2) + nums[idx],
                dfs(idx+1)
            )
            cache[idx] = ret
            #print(idx, ret)
            return ret
        return dfs(0)