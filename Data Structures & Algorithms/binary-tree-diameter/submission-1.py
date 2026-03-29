# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 
        def helper(current):
            if current is None:
                return 0
            lH = helper(current.left)
            rH = helper(current.right)
            self.res = max(self.res, lH + rH)
            return max(lH, rH) + 1

        helper(root)
        return self.res
        