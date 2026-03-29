class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        ans = []
        paran = [] # idx of open paran
        for c in s:
            if c == "(":
                ans.append("(")
                paran.append(len(ans)-1)
            elif c == ")":
                if len(paran) != 0:
                    paran.pop()
                    ans.append(")")
            else:
                ans.append(c)

        paran = set(paran)

        return "".join(c for i,c in enumerate(ans) if i not in paran )