# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque( [root] if root else [])
        ans = []
        rev = False
        while q:
            size = len(q)
            helper = [0] * size
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                idx = size - i - 1 if rev else i
                helper[idx] = node.val
            if not helper:
                continue
            ans.append(helper)
            rev = not rev
        return ans 