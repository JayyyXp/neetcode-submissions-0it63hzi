class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        nums.sort()
        l = 0
        ans = float('inf')
        for r in range(N):

            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                ans = min(
                    ans,
                    nums[r] - nums[l]
                )
        return ans
