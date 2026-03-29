# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo = {}
        def dfs(curr, canRob):
            if not curr:
                return 0
            if (curr, canRob) in memo:
                return memo[(curr, canRob)]
            if canRob:
                # try rob
                tryRob = curr.val + dfs(curr.left, False) + dfs(curr.right, False)
                # no try rob
                noRob = dfs(curr.left, True) + dfs(curr.right, True)

                ret = max(tryRob, noRob)
                memo[(curr, canRob)] = ret
                return ret
            else:
                noRob = dfs(curr.left, True) + dfs(curr.right, True)
                memo[(curr, canRob)] = noRob
                return noRob
        return dfs(root, True)