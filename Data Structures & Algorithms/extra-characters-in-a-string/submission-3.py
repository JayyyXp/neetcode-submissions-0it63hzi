class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dSet = set(dictionary)

        memo = {}
        def dfs(iS):
            if iS == len(s):
                return 0 
            if iS in memo:
                return memo[iS] 
            ret = 1+dfs(1+iS) # skip this char
            for j in range(iS, len(s)):
                if s[iS:j+1] in dSet:
                    ret = min(
                        ret,
                        dfs(j+1)
                    )
            memo[iS] = ret
            return ret
        return dfs(0)