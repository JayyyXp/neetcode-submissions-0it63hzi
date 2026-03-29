class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        M = len(boxGrid)
        N = len(boxGrid[0])
        ans = [["."]*M for _ in range(N)]

        for m in range(M):
            stoneSpot = N-1
            for n in reversed(range(N)):
                if boxGrid[m][n] == "*":
                    ans[n][M-m-1] = "*"
                    stoneSpot = n-1
                elif boxGrid[m][n] == "#":
                    ans[stoneSpot][M-m-1] = "#"
                    stoneSpot -= 1
            
        for n in range(N):
            print(ans[n])
        return ans 