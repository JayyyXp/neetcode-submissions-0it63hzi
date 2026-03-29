class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        dp = [[0,0] for _ in range(n)] # Alice Bob

        for i in range(n-1,-1,-1):
            for j in range(2):
                if j == 0:
                    ret = -float('inf')
                    for k in range(1,4):
                        prev = dp[i+k][1] if i+k < n else 0
                        ret = max(
                            sum(stoneValue[i:i+k]) + prev,
                            ret
                        )
                    dp[i][0] = ret
                else:
                    ret = float('inf')
                    for k in range(1,4):
                        prev = dp[i+k][0] if i+k < n else 0
                        ret = min(
                            prev,
                            ret
                        )
                    dp[i][1] = ret

        alice = dp[0][0]
        bob = sum(stoneValue) - alice
        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        return "Tie"
        