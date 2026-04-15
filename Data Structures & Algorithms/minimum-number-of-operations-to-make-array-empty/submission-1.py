class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        memo = [-1] * (max(counter.values()) + 1)
        def dfs(n):
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            if memo[n] != -1:
                return memo[n]
            ret = min(dfs(n-2), dfs(n-3)) + 1
            memo[n] = ret
            return ret 
            
        for e, c in counter.items():
            op = dfs(c)
            if op == float('inf'):
                return -1
            ans += op
        return ans