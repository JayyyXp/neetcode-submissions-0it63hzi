class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort()
        ans = 0
        for i in reversed(range(N)):
            cand = 1
            currUsed = 0
            for j in reversed(range(i)):
                if currUsed + nums[i] - nums[j] > k:
                    break 
                currUsed += nums[i] - nums[j]
                cand += 1
            ans = max(ans, cand)
        return ans 