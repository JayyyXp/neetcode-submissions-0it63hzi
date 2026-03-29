class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # ROWS
        i = 0 # ROWS
        m = len(matrix[0]) # COLS
        j = 0 # COLS
        while i < n:
            numS = matrix[i][j]
            numE = matrix[i][j+m-1]

            if target == numS or target == numE:
                return True
            elif target > numS and target < numE:
                while j < m :
                    if matrix[i][j] == target:
                        return True
                    j += 1
                return False
            else:
                i += 1
        return False