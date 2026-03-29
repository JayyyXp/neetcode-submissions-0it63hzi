import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        print(l,r)
        if not nums or l == len(nums) or nums[l] != target:
            l = -1
        if r-1 > -1 and nums[r-1] != target:
            r = -1
        else:
            r -= 1
        
        return [l, r]