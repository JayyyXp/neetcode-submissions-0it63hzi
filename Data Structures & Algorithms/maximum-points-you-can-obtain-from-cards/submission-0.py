class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        memo = {}
        def dfs(i,j,k):
            if k == 0:
                return 0
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            ret = max(
                dfs(i+1,j,k-1)+cardPoints[i],
                dfs(i,j-1,k-1)+cardPoints[j],
            )
            memo[(i,j,k)] = ret
            return ret

        return dfs(0,len(cardPoints)-1,k)