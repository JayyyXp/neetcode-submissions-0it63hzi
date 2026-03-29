# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        helper = {v:i for i,v in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return None
            root = TreeNode(val=postorder.pop())
            root.right = dfs(helper[root.val]+1, r)
            root.left = dfs(l, helper[root.val]-1)
            return root
        return dfs(0, len(inorder)-1)