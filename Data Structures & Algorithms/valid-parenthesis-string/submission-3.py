class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}
        def dfs(l, i):
            if i == len(s):
                return len(l) == 0
            if (l, i) in cache:
                return cache[(l,i)]
            #print(l, i)
            if s[i] == '(':
                cache[(l,i)] = dfs(l+'(', i+1) 
                return cache[(l,i)]
            elif s[i] == ')':
                if len(l) > 0 and l[-1] == '(':
                    cache[(l,i)] = dfs(l[:-1], i+1)
                    return cache[(l,i)]
                else:
                    cache[(l,i)] = False
                    return cache[(l,i)]
            else:
                cache[(l,i)] =  (
                    dfs(l,i+1) or # empty string
                    dfs(l+'(',i+1) or # add a open
                    (dfs(l[:-1], i+1))
                )
                return cache[(l,i)]

        return dfs("", 0)