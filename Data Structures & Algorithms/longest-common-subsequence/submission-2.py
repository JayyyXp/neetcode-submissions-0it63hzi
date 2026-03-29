class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)] 
            ret = 0
            if text1[i] == text2[j]:
                ret += dfs(i+1, j+1) + 1
            else:
                ret += max(dfs(i+1, j), dfs(i, j+1))
            cache[(i,j)] = ret
            return ret

        return dfs(0,0)