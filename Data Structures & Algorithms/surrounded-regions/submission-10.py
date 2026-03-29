class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        # 1) Capture the non-surrounded O's by setting to T's
        def capture(i, j):
            
            if (i < 0 or i == ROWS or
                j < 0 or j == COLS or
                board[i][j] != 'O'):
                return

            board[i][j] = 'T'
            capture(i + 1, j)
            capture(i - 1, j)
            capture(i ,j + 1)
            capture(i ,j -1)
        
        for i in range(COLS):
            # first row
            if board[0][i] == 'O':
                capture(0, i)
            # last row
            if board[ROWS - 1][i] == 'O':
                capture(ROWS - 1, i)
        
        for i in range(ROWS):
            # firs col
             if board[i][0] == 'O':
                capture(i, 0)
            # last col
             if board[i][COLS-1] == 'O':
                capture(i, COLS-1)


        # 2) Rest of the O's are surrounded change them to X's
        # 3) Change all T's to O's

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'