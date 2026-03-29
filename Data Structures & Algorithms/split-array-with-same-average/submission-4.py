class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        S = sum(nums)
        N = len(nums)
        possible = False
        for k in range(1, N):
            if (S * k) % N == 0:
                possible = True
                break
        if not possible:
            return False

        memo = {}
        def dfs(idx, rollSum, numChosen):
            if (idx, rollSum, numChosen) in memo:
                return memo[(idx, rollSum, numChosen)]
            if idx == N:
                if 0 < numChosen < N and rollSum * (N - numChosen) == (S - rollSum) * numChosen:
                    return True
                return False
            memo[(idx, rollSum, numChosen)] = (
                dfs(idx + 1, rollSum + nums[idx], numChosen+1) or 
                dfs(idx + 1, rollSum, numChosen)
            )
            return memo[(idx, rollSum, numChosen)]
        return dfs(0, 0,0)