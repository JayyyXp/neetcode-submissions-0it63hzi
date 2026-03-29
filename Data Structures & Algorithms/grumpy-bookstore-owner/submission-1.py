class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers)
        helper = [0] * N
        ans = 0
        for i in range(N):
            if grumpy[i]:
                helper[i] = customers[i]
            else:
                ans += customers[i]

        currSum = sum(helper[0:minutes])
        maxWindow = sum(helper[0:minutes])
        for r in range(minutes,N):
            currSum += helper[r]
            currSum -= helper[r-minutes]
            maxWindow = max(maxWindow, currSum)
        
        return ans + maxWindow