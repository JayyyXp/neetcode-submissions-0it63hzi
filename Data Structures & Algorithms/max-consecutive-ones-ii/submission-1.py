class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        idx_0 = -1
        for r in range(len(nums)):
            if nums[r] == 0:
                if idx_0 == -1:
                    idx_0 = r
                else:
                    # alread flipped one 0
                    ans = max(ans, r-l)
                    l = idx_0 + 1
                    idx_0 = r

        ans = max(ans, r-l+1)
        return ans