# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqualTree(curr, subCurr):
            if curr is None and subCurr is None:
                return True
            if ((curr is not None and subCurr is not None) and 
                (subCurr.val == curr.val) 
                ):
                return (isEqualTree(curr.left, subCurr.left) and
                isEqualTree(curr.right, subCurr.right))
            return False
        def dfs(curr, subroot):
            if curr is None:
                return False
            if subroot is None:
                return True
            if isEqualTree(curr, subroot):
                return True
            else:
                return dfs(curr.right, subroot) or dfs(curr.left, subroot) 
        return dfs(root, subRoot)