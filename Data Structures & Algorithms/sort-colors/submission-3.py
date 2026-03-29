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
            elif nums[i] == 2:
                j = len(nums) - 1
                i0 = -1
                while j > i:
                    if nums[j] == 1:
                        break
                    elif nums[j] == 0:
                        i0 = j
                        break
                    j -= 1
                if i0 == -1:
                    nums[j], nums[i] = nums[i], nums[j]
                else:
                    k = 0
                    while k < i:
                        if nums[k] == 1:
                            break
                        k += 1
                    if k == i:
                        nums[j], nums[i] = nums[i], nums[j]
                    else:
                        nums[i], nums[j], nums[k] = nums[k], nums[i], nums[j] 

