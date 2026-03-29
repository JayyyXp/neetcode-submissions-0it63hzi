class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= j:
                return True 
            if s[i] != s[j]:
                return False
            memo[i,j] = dfs(i+1,j-1)
            return memo[i,j]
        N = len(s)
        ii = 0
        jj = 0
        for i in range(N):
            for j in range(i+1,N):
                if dfs(i,j):
                    if jj - ii < j - i:
                        ii = i
                        jj = j
        return s[ii:jj+1]      