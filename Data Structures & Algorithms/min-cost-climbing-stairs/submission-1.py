class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def climb(idx):
            print(idx)
            if idx >= len(cost):
                return 0
            if idx in cache:
                return cache[idx]
            c1 = climb(idx+1)
            c2 = climb(idx+2)
            ret = min(c1, c2) + cost[idx]
            cache[idx] = ret 
            return ret
        
        return min(climb(0), climb(1))