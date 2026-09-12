class Solution:
    def maxDepth(self, s: str) -> int:
        
        ans, stack = 0, 0
        for c in s:
            if c == "(":
                stack += 1
            elif c == ")":
                stack -= 1

            ans = max(ans, stack)
        return ans