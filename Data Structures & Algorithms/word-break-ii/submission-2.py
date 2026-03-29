class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wD = set(wordDict)
        ans = []
        helper = []
        def dfs(start):
            if start == len(s):
                ans.append(" ".join(helper))
                return
            for i in range(start, len(s)):
                if s[start:i+1] in wD:
                    helper.append(s[start:i+1])
                    dfs(i+1)
                    helper.pop()


        dfs(0)
        return ans