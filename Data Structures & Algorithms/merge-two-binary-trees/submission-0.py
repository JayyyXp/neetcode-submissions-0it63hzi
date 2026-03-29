# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(h1,h2):
            if not h1 and not h2:
                return None
            if not h1:
                return h2
            if not h2:
                return h1
            h1.val += h2.val
            h1.left = dfs(h1.left,h2.left)
            h1.right = dfs(h1.right,h2.right)
            return h1
        return dfs(root1,root2)