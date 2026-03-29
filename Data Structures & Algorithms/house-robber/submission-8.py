class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums)
        if n <= 2:
            return max(nums)
        #dp = [0] * n
        dp_0 = nums[0]
        dp_1 = max(nums[0], nums[1])#nums[1]

        for i in range(2, n):
            dp_2 = max(
                dp_0 + nums[i],
                dp_1
            )
            dp_0 = dp_1
            dp_1 = dp_2
        return dp_2