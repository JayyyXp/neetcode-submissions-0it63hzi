class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 1:
            return nums
        nums.sort()
        k = 0
        for i,j in zip(range(N//2), reversed(range(N//2, N))):
            nums[i] = [nums[i], k]
            k += 1
            nums[j] = [nums[j], k]
            k += 1
        if N % 2 == 1:
            nums[(N//2)] = [nums[(N//2)], k]
        print(nums)
        nums.sort(key=lambda x: x[1])
        
        for i in range(N):
            nums[i] = nums[i][0]