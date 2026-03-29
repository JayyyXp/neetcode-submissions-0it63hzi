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
            # We can split between i and len(nums) - k (to leave room for remaining k-1 groups)
            for j in range(i, len(nums) - k+1):
                total += nums[j]
                ret = min(
                    ret,
                    max(
                        dfs(j + 1, k-1),
                        total
                    )
                )
                # pruning: if total already exceeds current best, stop early
                if total > ret:
                    break
            memo[(i,k)] = ret  
            return ret 
        return dfs(0,k)