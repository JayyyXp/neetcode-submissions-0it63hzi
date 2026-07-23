class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = 9
        COLS = 9
        def isValid(counter):
            counter.pop(".", None)
            return any(c > 1 for n, c in counter.items() )

        for r in range(ROWS):
            counter = Counter(board[r])
            if isValid(counter):
                return False

        for c in range(COLS):
            counter = Counter([board[r][c] for r in range(ROWS)])
            if isValid(counter):
                return False

        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                helper = [
                    board[rr][cc]
                    for rr in range(r, r + 3)
                    for cc in range(c, c + 3)
                ]
                counter = Counter(helper)
                if isValid(counter):
                    return False
                
        return True 