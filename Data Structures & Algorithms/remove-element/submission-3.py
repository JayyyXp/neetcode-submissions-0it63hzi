class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) -1
        k = 0
        while j > -1 and nums[j] == val:
            j -= 1
        i = 0
        while i <= j:
            if nums[i] == val:
                # Swap with current valid j
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                # Move j to next valid position
                while j >= i and nums[j] == val:
                    j -= 1
            else:
                i += 1

        return j + 1