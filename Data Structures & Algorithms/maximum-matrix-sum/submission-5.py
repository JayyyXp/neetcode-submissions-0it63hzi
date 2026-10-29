class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        import heapq
        # -1 -2 -3
        #  3  4  5
        #  3  4  5


        ROWS = len(matrix)
        COLS = len(matrix[0])

        nbrminus = 0
        min_abs = float('inf')
        s = 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] < 0:
                    nbrminus += 1
                min_abs = min(min_abs, abs(matrix[r][c]))
    
                s += abs(matrix[r][c])
                
        if nbrminus % 2 == 0:
            return s

        return s - 2*min_abs
