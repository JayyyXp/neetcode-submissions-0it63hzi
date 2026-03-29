class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wD = set(wordDict)
        ans = []

        def dfs(start, sent):
            if start == len(s):
                ans.append(" ".join(sent))
                return
            for i in range(start, len(s)):
                if s[start:i+1] in wD:
                    dfs(i+1, sent + [s[start:i+1]])


        dfs(0, [])
        return ans