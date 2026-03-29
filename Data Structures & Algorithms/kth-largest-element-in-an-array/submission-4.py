class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums
        import heapq

        heapq.heapify(q)
        ans = 0
        for _ in range(len(nums)-k+1):
            ans = heapq.heappop(q)
            print(ans)
        
        return ans