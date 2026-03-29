class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        for i, n in enumerate(nums):
            prod *= n
        ans = nums.copy()
        for i, n in enumerate(nums):
            if n == 0:
                ans[i] = 1
                for j, nn in enumerate(nums):
                    if j != i:
                       ans[i] *= nn  
            else:
               ans[i] = int(prod / n)

        return ans

        