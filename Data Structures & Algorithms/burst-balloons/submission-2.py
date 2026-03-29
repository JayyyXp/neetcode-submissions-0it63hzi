class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        ans = [0]
        cache = set()

        def dfs(available,curr):
            #print(available,curr,ans[0])
            if len(available) == 0:
                if curr > ans[0]:
                    ans[0] = curr
                return
            if (tuple(available),curr) in cache:
                return 
            for i, n in enumerate(available):
                nxt = 1
                if i+1 < len(available):
                    nxt = available[i+1] 
                prv = 1
                if i-1 > -1:
                    prv = available[i-1] 
                dfs(
                    available[:i] + available[i+1:], 
                    curr+prv*available[i]*nxt
                )  
            cache.add((tuple(available),curr))
        dfs(nums, 0)

        return ans[0]