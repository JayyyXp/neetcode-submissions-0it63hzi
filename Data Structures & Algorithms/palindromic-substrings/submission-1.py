class Solution:
    def countSubstrings(self, s: str) -> int:
        sr = s[::-1]
        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            ret = 0 
            if s[l:r+1] == sr[len(s)-r-1:len(s) - l]:
                ret += 1
            ret += dfs(l + 1, r) + dfs(l, r-1) - dfs(l + 1, r - 1)
            cache[(l,r)] = ret
            return ret

        return dfs(0, len(s)-1)