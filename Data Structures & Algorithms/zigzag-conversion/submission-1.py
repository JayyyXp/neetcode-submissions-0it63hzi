class Solution:
    def convert(self, s: str, numRows: int) -> str:
        down = True # False means zigzag
        ans = [[] for _ in range(numRows)]
        r = 0
        for c in s:
            ans[r].append(c)
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
        return "".join("".join(r) for r in ans )