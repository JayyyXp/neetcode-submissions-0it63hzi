class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = [-1] * len(days)
        def dfs(i):
            if i >= len(days):
                return 0
            if memo[i] != -1:
                return memo[i] 
            # one day ticket
            ret = dfs(i+1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            
            ret = min(
                ret,
                dfs(j) + costs[1]
            ) 
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
        
            ret = min(
                ret,
                dfs(j) + costs[2]
            ) 
            
            memo[i] = ret
            return ret


        return dfs(0)


