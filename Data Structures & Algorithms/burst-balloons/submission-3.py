class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        ans = [0]
        cache = {}

        def dfs(available):
            #print(available,curr,ans[0])
            if len(available) == 1:
                return available[0]
            if tuple(available) in cache:
                return cache[tuple(available)]
            ret = 0
            for i, n in enumerate(available):
                nxt = 1
                if i+1 < len(available):
                    nxt = available[i+1] 
                prv = 1
                if i-1 > -1:
                    prv = available[i-1] 
                ret = max(
                    ret,
                    dfs(
                        available[:i] + available[i+1:]
                    ) + prv*available[i]*nxt
                )
            cache[tuple(available)] = ret
            return ret
     

        return   dfs(nums)