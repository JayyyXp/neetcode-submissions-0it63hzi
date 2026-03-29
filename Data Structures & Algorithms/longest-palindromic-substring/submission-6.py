class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ababd
        # dbaba
        helper = [""]
        visited = set()
        def dfs(start,end):
            if start == end:
                return
            if s[start:end] in visited:
                return
            if s[start:end] == s[start:end][::-1]:
                if len(helper[0]) < len(s[start:end]):
                    helper[0] = s[start:end]
            visited.add(s[start:end])
            dfs(start+1, end)
            dfs(start, end-1)

        dfs(0, len(s))
        return helper[0]

