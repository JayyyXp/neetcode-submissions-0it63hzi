class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        curr = 1
        ans = 0
        for r in range(N):

            curr *= nums[r] 
            #print(nums[l:r+1])
            while l <= r and curr >= k:
                curr //= nums[l]
                l += 1

            ans += (r-l+1) 

        return ans