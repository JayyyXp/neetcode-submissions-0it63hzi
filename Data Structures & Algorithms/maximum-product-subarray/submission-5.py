class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prefix = 1
        suffix = 1
        res = -float('inf')

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums)-1-i]
            res = max(
                res,
                prefix,
                suffix
            )
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return res