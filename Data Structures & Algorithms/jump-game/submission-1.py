class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        numLast = len(nums) - 1

        def helper(i):
            if i == numLast:
                return True 
            availableJumps = nums[i]

            for jump in range(1, availableJumps + 1):
                if helper(i + jump):
                    return True
            return False
        return helper(0)
