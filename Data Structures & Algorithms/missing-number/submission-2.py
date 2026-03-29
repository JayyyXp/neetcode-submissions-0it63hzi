class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        helper = 0
        for num in nums:
            if num == helper:
                helper += 1
            else:
                return helper
        return helper