class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        ans = []
        l = {}
        for char, count in zip(["a","b","c"],[a,b,c]):
            if count > 0:
                l[char] = count  
        for _ in range(a+b+c):
            if len(l) == 0:
                break
            m = max(l, key=l.get)
            if len(ans) > 1 and ans[-2] == ans[-1] == m:
                newM = max(l, key=lambda x: -1 if x == m else l[x])
                print(m)
                if m == newM:
                    break
                ans.append(newM)
                l[newM] -= 1
                if l[newM] == 0:
                    del l[newM]
            else:
                ans.append(m)
                l[m] -= 1
                if l[m] == 0:
                    del l[m]

        return "".join(ans) 
