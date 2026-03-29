class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()
        ans = []
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        currR = 0
        currC = 0
        d = 0
        while True:
            visited.add((currR,currC))
            ans.append(matrix[currR][currC])
            cont = False
            for i in range(4):
                dr, dc = dirs[(d+i) % 4]
                if (
                    (currR + dr) in range(ROWS) and 
                    (currC + dc) in range(COLS) and
                    (currR + dr, currC + dc) not in visited
                    ):
                    d = (d+i) % 4
                    currR += dr
                    currC += dc
                    cont = True
                    break
            if not cont:
                break
            

        return ans