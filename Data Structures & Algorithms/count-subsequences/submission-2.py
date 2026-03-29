class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(idxS, idxT):
            if idxT >= len(t):
                return 1
            if idxS >= len(s):
                return 0
            if (idxS, idxT) in cache:
                return cache[(idxS, idxT)]
            ret = 0
            for iS in range(idxS, len(s)):
                if s[iS] == t[idxT]:
                    ret += dfs(iS+1, idxT+1)
            cache[(idxS, idxT)] = ret
            return ret
        return dfs(0,0)