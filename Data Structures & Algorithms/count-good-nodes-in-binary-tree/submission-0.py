# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr, lastGood):
            if curr is None:
                return 0
            if curr.val >= lastGood:
                return dfs(curr.left, curr.val) + dfs(curr.right, curr.val) + 1
            else:
                return dfs(curr.left, lastGood) + dfs(curr.right, lastGood)

        return dfs(root, root.val)