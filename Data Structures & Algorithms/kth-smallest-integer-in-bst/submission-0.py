# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        def dfs(curr):
            if not curr:
                return
            heapq.heappush(minHeap, curr.val)
            dfs(curr.left)
            dfs(curr.right)
            
        dfs(root)

        ans = 0
        for i in range(k):
            ans = heapq.heappop(minHeap)
        return ans
