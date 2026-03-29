class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # aabcb
        # abbab

        allSubS = []
        def dfs(idx, l):
            if idx == len(s):
                #print(l)
                allSubS.append(l)
                return
            addToLast = list(l)
            addToLast[-1] = f"{addToLast[-1]}{s[idx]}" 
            dfs(idx+1, addToLast)
            if l[-1] != "":
                addNewLast = list(l)
                addNewLast.append(s[idx])
                dfs(idx+1, addNewLast)

        dfs(0, [""])
        print(allSubS)
        ans = []
        for subs in allSubS:
            add = True
            for sub in subs:
                if sub != sub[::-1]:
                    add = False
                    break
            if add:
                ans.append(subs)
        return ans 
