class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        print(wordDict)
        l, r = 0, 0

        #while r <= len(s) - 1:
        #    cand = s[l:r+1]
        #    if cand in wordDict:
        #        print(cand)
        #        l = r +1
        #        r = l
        #    else:
        #        r += 1
        cache = {}
        def dfs(l, r):
            if r > len(s) - 1:
                return l == len(s)
            if (l,r) in cache:
                return cache[(l,r)]
            cand = s[l:r+1]
            retFound = False
            retNext = dfs(l, r+1)
            if cand in wordDict:
                print(cand)
                l = r +1
                r = l
                retFound = dfs(l, r)
            ret = retNext or retFound
            cache[(l, r)] = ret
            return ret

        return dfs(0,0)

        