class Solution:
    def convert(self, s: str, numRows: int) -> str:
        down = True # False means zigzag
        col = [[] for _ in range(numRows)]
        print(col)
        r = 0
        for c in s:
            col[r].append(c)
            if down:
                r += 1
                if r == numRows:
                    down = False
                    r = numRows - 2
            else:
                r -= 1
                if r == -1:
                    down = True
                    r = 1
        ans = []
        for r in col:
            ans.extend(r)
        return "".join(ans)