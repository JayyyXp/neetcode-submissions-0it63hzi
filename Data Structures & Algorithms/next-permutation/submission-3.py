class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        N = len(nums)
        if N == 1:
            return
        for i in range(N-2,-1,-1):
            if nums[i] < nums[i+1]:
                break

        if i == 0:
            nums.reverse()
            return

        for j in range(N-1,-1,-1):
            if nums[i] < nums[j]:
                break

        nums[i], nums[j] = nums[j], nums[i]

        
        nums[i+1:] = reversed(nums[i+1:]) 

