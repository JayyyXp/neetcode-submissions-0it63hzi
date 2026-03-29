class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        heapq.heapify(heap)

        for n in arr:
            heapq.heappush(heap, [abs(x - n), n])
        ans = []
        for i in range(k):
            n = heapq.heappop(heap)[1]
            if len(ans) == 0:
                ans.append(n)
            elif ans[-1] <= n:
                ans.append(n)
            else:
                ans = [n] + ans
        return ans