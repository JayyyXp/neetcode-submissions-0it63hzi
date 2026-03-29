class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def helper(o, c, s):
            if n == o == c:
                ans.append(s)
                return
            if o < n:
                helper(o + 1, c, s + "(")
            if c < o:
                helper(o, c + 1, s + ")")
        
        helper(0,0, "")
        return ans
