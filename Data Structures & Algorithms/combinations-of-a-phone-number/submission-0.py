class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        helper = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        if len(digits) == 0:
            return []

        def dfs(i, currStr):
            if i == len(digits):
                ans.append(currStr)
                return
            for nextChar in helper[digits[i]]:
                dfs(i+1, currStr + nextChar)
            

        dfs(0, "")
        return ans