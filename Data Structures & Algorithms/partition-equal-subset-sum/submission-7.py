class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cache = {}
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        def dfs(idx,sum1):
            if sum1 == target:
                return True
            #if len(subset1) == 0:
            if sum1 > target or idx == len(nums):  
                return False
            if (idx,sum1) in cache:
                return cache[(idx,sum1)]
            ret = False
            if dfs(idx+1,sum1+nums[idx]):
                ret = True
            if dfs(idx+1, sum1):
                ret = True
            cache[(idx,sum1)] = ret
            return ret

        return dfs(0, 0)