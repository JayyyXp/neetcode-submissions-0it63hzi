# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def dfs(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            
            root = TreeNode(val=preorder[0])
            inorderIdx = inorder.index(root.val)
            leftInorderLen = len(inorder[:inorderIdx])
            root.left = dfs(preorder[1:leftInorderLen+1],inorder[:inorderIdx])
            root.right = dfs(preorder[leftInorderLen+1:],inorder[inorderIdx+1:])

            return root

        return dfs(preorder, inorder)    