# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = [root.val]

        def helper(node):
            if node is None:
                return 0
            lA = max(helper(node.left), 0)
            rA = max(helper(node.right), 0)

            ans[0] = max(
                lA + rA + node.val,
                ans[0]
            )
            return node.val + max(lA, rA, 0)


        helper(root)
        return ans[0] 
        