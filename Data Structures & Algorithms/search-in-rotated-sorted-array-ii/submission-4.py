class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l,r = 0, len(nums)-1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return True
            # left side sorted
            if nums[l] < nums[m]:
                # target in sorted portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right side sorted
            elif nums[l] > nums[m]:  # Right portion
                # target in sorted portion
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False