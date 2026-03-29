class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0] * 3
        for n in nums:
            count[n] += 1
        i = 0
        print(count)
        for j, c in enumerate(count):
            while c:
                nums[i] = j
                i += 1
                c -= 1
                
