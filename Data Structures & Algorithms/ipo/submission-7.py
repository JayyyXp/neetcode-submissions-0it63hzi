class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c,p)for c,p in zip(capital, profits)]
        maxHeap = []
        heapq.heapify(minHeap)
        heapq.heapify(maxHeap)

        for i in range(k):
            while minHeap and minHeap[0][0] <= w:
                c,p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, -p)
            if not maxHeap:
                break
            p = heapq.heappop(maxHeap)
            w += -p
        return w