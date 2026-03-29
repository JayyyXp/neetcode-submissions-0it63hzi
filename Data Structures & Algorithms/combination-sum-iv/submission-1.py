class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(s):
            if s == target:
                return 1
            if s > target:
                return 0
            if s in memo:
                return memo[s]
            ret = 0
            for n in nums:
                ret += dfs(s+n)
            memo[s] = ret
            return ret

        return dfs(0)