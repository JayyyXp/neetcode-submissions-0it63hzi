class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if nums[i] == 0:
                j = 0
                while j < i:
                    if nums[j] != 0:
                        break
                    j += 1
                nums[j], nums[i] = nums[i], nums[j]
                print(nums[i], nums[j])
                print(nums)
        for i in range(len(nums)):
            if nums[i] == 2:
                j = len(nums) - 1
                while j > i:
                    if nums[j] != 2:
                        break
                    j -= 1
                nums[j], nums[i] = nums[i], nums[j]
                print(nums[i], nums[j])
                print(nums)