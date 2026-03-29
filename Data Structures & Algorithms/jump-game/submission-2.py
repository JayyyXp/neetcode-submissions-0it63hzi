class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        numLast = len(nums) - 1
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i == numLast:
                memo[i] = True
                return True 
            availableJumps = nums[i]
            for jump in range(1, availableJumps + 1):
                if helper(i + jump):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return helper(0)
