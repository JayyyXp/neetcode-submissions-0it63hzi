class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        s = sum(mat[i][i] for i in range(N))
        s += sum(mat[N-1-i][i] for i in range(N))
        if N % 2 == 0:
            return s
        return s - mat[N//2][N//2]
        