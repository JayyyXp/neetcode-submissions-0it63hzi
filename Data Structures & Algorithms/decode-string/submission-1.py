class Solution:
    def decodeString(self, s: str) -> str:
        
        ans = ""
        num = ""
        helper = ""
        addToHelp = False

        def dfs(i, ans, num):
            if i == len(s):
                return ans, i
            c = s[i]
            if c in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                return dfs(i+1, ans, num+c)
            if c == "[":
                subadd, i = dfs(i+1, "", "")
                return dfs(i+1, ans+(int(num)*subadd), "")
            if c == "]":
                return ans, i
            return dfs(i+1, ans+c, num)

        return dfs(0, "", "")[0]

