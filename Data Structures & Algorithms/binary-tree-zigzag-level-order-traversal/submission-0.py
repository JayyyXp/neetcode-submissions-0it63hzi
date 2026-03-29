# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque([root])
        ans = []
        rev = False
        while q:
            helper = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                helper.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if not helper:
                continue
            if rev:
                ans.append(list(reversed(helper)))
            else:
                ans.append(list(helper))
            rev = not rev
        return ans 