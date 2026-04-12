class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        ans = 0
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                right = dp[r][c+1] if c + 1 < COLS else 0
                down = dp[r+1][c] if r + 1 < ROWS else 0
                diag = dp[r+1][c+1] if c + 1 < COLS and r + 1 < ROWS else 0

                if matrix[r][c] == "1":
                    dp[r][c] = min(
                        right,
                        down,
                        diag,
                    ) + 1
                else:
                    dp[r][c] = 0
                ans = max(ans, dp[r][c] * dp[r][c])
                #print(ans, dp[r][c], right, down, diag)
        return ans