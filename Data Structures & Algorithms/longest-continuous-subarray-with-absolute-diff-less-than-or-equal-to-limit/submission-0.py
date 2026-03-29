class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        l = 0
        minHeap = []
        maxHeap = []
        ans = 0
        for r in range(N):
            heapq.heappush(minHeap, [nums[r], r])
            heapq.heappush(maxHeap, [-nums[r], r])

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l += 1
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)
            ans = max(ans, r - l + 1)

        return ans