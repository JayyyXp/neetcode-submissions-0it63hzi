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


        return dfs(0,0)