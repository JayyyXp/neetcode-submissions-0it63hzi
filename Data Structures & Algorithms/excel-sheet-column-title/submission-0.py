class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = deque()
        while columnNumber > 0:
            columnNumber -= 1  # fix off-by-one
            print(columnNumber)
            n = columnNumber % 26
            columnNumber //= 26
            c = chr(ord('A') + n)
            ans.appendleft(c)
        return "".join(ans)