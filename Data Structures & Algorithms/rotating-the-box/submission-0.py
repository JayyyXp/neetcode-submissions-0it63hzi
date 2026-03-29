class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        M = len(boxGrid)
        N = len(boxGrid[0])
        ans = [["."]*M for _ in range(N)]

        for m in range(M):
            stoneSpot = deque()
            for n in reversed(range(N)):
                if boxGrid[m][n] == "*":
                    ans[n][M-m-1] = "*"
                    stoneSpot = deque()
                elif boxGrid[m][n] == "#":
                    if stoneSpot:
                        ans[stoneSpot.popleft()][M-m-1] = "#"
                        stoneSpot.append(n)
                    else:
                        ans[n][M-m-1] = "#"
                else:
                    stoneSpot.append(n)
            
        for n in range(N):
            print(ans[n])
        return ans 