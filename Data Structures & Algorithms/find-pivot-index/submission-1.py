class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        sum_l = sum(nums)
        sum_r = 0
        coolDown = 0
        for i,n in enumerate(nums):
            sum_r += coolDown
            coolDown = n 
            sum_l -= n
            if sum_r == sum_l:
                return i
        return -1

