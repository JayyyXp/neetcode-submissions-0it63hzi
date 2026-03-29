class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        def dfs(cornerI, cornerJ,n):
            if n <= 1:
                return 
            dirs = [[0, n - 1], [n - 1, 0], [0, -(n - 1)], [-(n - 1), 0]]
            for i in range(0,n-1):
                tempI, tempJ = cornerI, cornerJ+i
                tempVal = matrix[tempI][tempJ]
                #print(tempVal)
                #print(dirs)
                for j, (di, dj) in enumerate(dirs):
                    print(tempVal, di, dj, matrix[tempI + di][tempJ + dj])
                    #for ii in range(n):
                    #    print(matrix[ii])
                    #print()
                    tempVal, matrix[tempI + di][tempJ + dj] = matrix[tempI + di][tempJ + dj], tempVal
                    tempI, tempJ = tempI + di, tempJ + dj
                    if j == 0:
                        dirs[j][0] += 1
                        dirs[j][1] -= 1
                    if j == 1:
                        dirs[j][0] -= 1
                        dirs[j][1] -= 1
                    if j == 2:
                        dirs[j][0] -= 1
                        dirs[j][1] += 1
                    if j == 3:
                        dirs[j][0] += 1
                        dirs[j][1] += 1
                #for ii in range(n):
                    #print(matrix[ii])
                #print()
            dfs(cornerI+1, cornerJ+1,n-2)

        dfs(0,0,n)