class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        ans = ""
        l = {}
        for char, count in zip(["a","b","c"],[a,b,c]):
            if count > 0:
                l[char] = count  
        print(l)
        for _ in range(a+b+c):
            if len(l) == 0:
                return ans
            m = max(l, key=l.get)
            if len(ans) > 1 and ans[-2] == ans[-1] == m:
                cooldown = [m , l[m]]
                del l[m]
                if len(l) == 0:
                    return ans
                m = max(l, key=l.get)
                ans += m
                l[m] -= 1
                if l[m] == 0:
                    del l[m]
                l[cooldown[0]] = cooldown[1]
            else:
                ans += m
                l[m] -= 1
                if l[m] == 0:
                    del l[m]

        return ans 
