class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def validNines(nines):
            # valid digits
            #for n in nines:
            #    if n not in range(0,10):
            #        return False
            # No dublicates
            seen = set()
            for n in nines:
                if n != '.':
                    if n not in seen:
                        seen.add(n)
                    else:
                        return False
            return True
        # Check each row 
        for r in range(ROWS):
            if not validNines(board[r]):
                print('not valid', board[r])
                return False
        # Check each col
        for c in range(COLS):
            col = [0] * 9
            for r in range(ROWS):
                col[r] = board[r][c]
            if not validNines(col):
                print('not valid', col)
                return False
        # Check each square
        squareCenter = [
            [1,1], [1,4], [1,7],
            [4,1], [4,4], [4,7],
            [7,1], [7,4], [7,7],
        ]
        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 0], [0, 1],
            [1, -1], [1, 0], [1, 1],
        ]
        for r, c in squareCenter:
            square = [
                board[r+dr][c+dc]
                for dr, dc in directions 
            ]
            if not validNines(square):
                print('not valid', square)
                return False
        return True
