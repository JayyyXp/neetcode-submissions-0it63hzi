# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = 0
        def dfs(node):
            if not node:
                return False, False
            p1,q1 = dfs(node.left)
            p2,q2 = dfs(node.right)
            p_seen = True if node.val == p.val else False
            q_seen = True if node.val == q.val else False  

            p_seen = p_seen or p1 or p2 
            q_seen = q_seen or q1 or q2 
            print(node.val, p_seen, q_seen)
            if p_seen and q_seen:
                self.ans = node
                return False, False
            return p_seen, q_seen

        dfs(root)
        return self.ans 