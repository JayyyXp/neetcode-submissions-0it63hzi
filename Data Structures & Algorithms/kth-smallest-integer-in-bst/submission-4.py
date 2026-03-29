# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minHeap = []
        #heapq.heapify(minHeap)

        def dfs(curr):
            if not curr or len(minHeap) == k+1 :
                return
            dfs(curr.left)
            minHeap.append(curr.val)
            #heapq.heappush(minHeap, curr.val)
            dfs(curr.right)

        dfs(root)

        #ans = 0
        #for i in range(k):
        #    ans = heapq.heappop(minHeap)
        #return ans
        return minHeap[k-1]
