class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        l = 0
        minq = deque() # mono increasing
        maxq = deque() # mono decreasing
        ans = 0
        for r in range(N):
            while minq and minq[-1][0] > nums[r]:
                minq.pop()
            while maxq and maxq[-1][0] < nums[r]:
                maxq.pop()
            maxq.append([nums[r], r])
            minq.append([nums[r], r])
            
            while maxq[0][0] - minq[0][0] > limit:
                l += 1
                while maxq[0][1] < l:
                    maxq.popleft()
                while minq[0][1] < l:
                    minq.popleft()
            ans = max(ans, r - l + 1)

        return ans