class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappop, heappush, heapify

        l, r = 0, k-1
        ans = []
        heap = []
        heapify(heap)
        for i in range(k):
            heappush(heap,[-nums[i], i])

        while True:
            while True:
                val, idx = heap[0]
                if idx not in range(l,r+1):
                    # if max not in sliding window, pop max
                    heappop(heap)
                else:
                    ans.append(-val)
                    break


            r += 1
            if not (r < len(nums)):
                break
            heappush(heap, [-nums[r], r])
            l += 1

        return ans