# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ans =[True] 
    
        def dfs(node):
            if not node:
                return 0

            hl = dfs(node.left)
            hr = dfs(node.right)
            print(node.val, hl, hr)
            if abs(hl - hr) > 1:
                ans[0] = False

            return max(hl, hr) + 1
        dfs(root)
        return ans[0]