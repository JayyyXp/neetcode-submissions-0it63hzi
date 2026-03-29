# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [0]
        def dfs(curr):
            if curr is None:
                return 0
            ret = 0
            ret += dfs(curr.left) + dfs(curr.right)
            if curr.val == p.val:
                ret += 1 
            elif curr.val == q.val:
                ret += 1 
            if ret == 2:
                lca[0] = curr
                ret = 0
            return ret
            
        dfs(root)
        return lca[0]
             