"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        def dfs(curr):
            if curr is None:
                return 

            for child in curr.children:
                dfs(child)
                ans.append(child.val)
        dfs(root)
        if root:
            ans.append(root.val)
        return ans