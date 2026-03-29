# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs1(curr):
            if curr is None:
                return False
            if curr.val == subRoot.val:
                ret = dfs2(curr, subRoot)
                if ret:
                    return ret
            
            ret = dfs1(curr.left)
            if ret:
                return ret
            ret = dfs1(curr.right)
            if ret:
                return ret
            return False
            
            
        def dfs2(curr1, curr2):
            if not curr1 and not curr2:
                return True 
            if not curr1 and curr2:
                return False
            if curr1 and not curr2:
                return False
            if curr1.val != curr2.val:
                return False
            return dfs2(curr1.left, curr2.left) and dfs2(curr1.right, curr2.right) 
        
        return dfs1(root)
   