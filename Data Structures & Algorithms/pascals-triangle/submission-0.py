class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        new_row = []
        for _ in range(numRows-1):
            for i in range(len(ans[-1])+1):
                prev = ans[-1][i-1] if i-1 > -1 else 0
                top = ans[-1][i] if i < len(ans[-1]) else 0
                new_row.append(prev+top)
            ans.append(new_row)
            new_row = []
        return ans