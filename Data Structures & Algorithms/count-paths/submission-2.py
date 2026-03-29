class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        visited = set()
        def dfs(i, j):
            if (m == i or 
                i == -1 or 
                n == j or 
                j == -1 or 
                (i,j) in visited
            ):
                return 0
            if i == (m - 1) and j == (n - 1):
                return 1
            
            ret = 0
            visited.add((i,j))
            ret += dfs(i+1, j)
            #ret += dfs(i-1, j)
            ret += dfs(i, j+1)
            #ret += dfs(i, j-1)
            visited.remove((i,j))
            return ret


        #return dfs(0,0)

        #dp = [[0]*(n+1) for i in range(m+1)]
        #dp[1][1] = 1
        dp1 = [0]*(n+1)
        dp1[1] = 1
        for i in range(1, m+1):
            dpNew = [0]*(n+1)
            for j in range(1, n+1): 
                #dp[i][j] = dp[i][j-1] + dp[i-1][j] + dp[i][j]
                dpNew[j] = dpNew[j-1] + dp1[j]
            dp1 = dpNew
        #print(dp)
        #return dp[-1][-1]
        return dp1[-1]