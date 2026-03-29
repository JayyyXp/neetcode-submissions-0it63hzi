class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        e = 0
        for i,n in enumerate(nums):
            if n % 2 == 0:
                while e < len(nums) and nums[e] % 2 == 0:
                    e += 1
                if e < len(nums) and e < i:
                    nums[i], nums[e] = nums[e], nums[i]
        return nums     
           

        