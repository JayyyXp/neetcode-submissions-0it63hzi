class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            ret = 0
            if text1[i] == text2[j]:
                ret = 1 + dp(i+1, j+1)
            else:
                ret = max(
                    dp(i+1, j),
                    dp(i, j+1)
                )
            memo[(i, j)] = ret
            return ret
        return dp(0,0)