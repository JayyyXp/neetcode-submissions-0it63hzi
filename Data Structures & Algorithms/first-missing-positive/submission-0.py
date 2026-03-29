class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nSet = set(nums)
        curr = 1
        while True:
            if curr not in nSet:
                return curr
            curr += 1