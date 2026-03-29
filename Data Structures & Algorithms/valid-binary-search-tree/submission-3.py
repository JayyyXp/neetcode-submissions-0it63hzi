# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        def dfs(node, l, r):
            if not node:
                return
            if not(l < node.val < r):
                ans[0] = False
                return
            dfs(node.left, l, node.val) 
            dfs(node.right, node.val, r) 
            

        dfs(root, -1001, 1001)
        return ans[0]