class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        ans = []
        helper = []

        def dfs(i):
            if i == len(s):
                ans.append(" ".join(helper))
                return
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    helper.append(s[i:j+1])
                    dfs(j+1)
                    helper.pop()

        dfs(0)
        return ans

        