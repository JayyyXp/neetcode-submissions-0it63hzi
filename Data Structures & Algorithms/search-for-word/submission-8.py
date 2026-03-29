class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def search(r, c, idx):

            if (r == -1 or r == ROWS or
                c == -1 or c == COLS or
                idx == len(word) or
                (r,c) in visited or
                board[r][c] != word[idx]
            ):
                return False
            if idx == len(word) - 1 and board[r][c] == word[idx]:
                return True
            visited.add((r,c))
            found = (search(r+1, c, idx + 1) or 
                    search(r-1, c, idx + 1) or 
                    search(r, c+1, idx + 1) or 
                    search(r, c-1, idx + 1))
            # This ensures that the same cell can be reused in other search paths,
            # just not within the same one.
            visited.remove((r, c))
            return found
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visited = set()
                    if search(r, c, 0):
                        return True 

        return False