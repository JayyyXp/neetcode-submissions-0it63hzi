class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        s = 0
        for i in range(N):
            s += mat[i][i]
            s += mat[N-1-i][i]
        if N % 2 == 0:
            return s
        return s - mat[N//2][N//2]
        