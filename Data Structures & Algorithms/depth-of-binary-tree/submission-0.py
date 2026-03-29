# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverser(tree, current):
            if tree is None:
                return current
            return max(traverser(tree.left, current+1), traverser(tree.right, current+1))
        
        return traverser(root, 0)
        