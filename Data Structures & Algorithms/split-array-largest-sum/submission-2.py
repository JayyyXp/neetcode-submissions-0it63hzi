class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        memo = {}
        def dfs(i, k):
            if k == 1:
                return sum(nums[i:])
            if (i,k) in memo:
                return memo[(i,k)]
            ret = float('inf')
            total = 0
            for j in range(i, len(nums) - k+1):
                total += nums[j]
                ret = min(
                    ret,
                    max(
                        dfs(j + 1, k-1),
                        total
                    )
                )
            memo[(i,k)] = ret
            return ret 
        return dfs(0,k)