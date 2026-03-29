class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        changed = False
        minval = float('inf')
        for i in range(len(nums)-1):
            minval = min(minval, nums[i])
            if not (nums[i] <= nums[i+1]):
                changed = True
                break
        if changed:
            for j in range(i+1, len(nums)):
                if nums[j] > minval:
                    return False
        return True 