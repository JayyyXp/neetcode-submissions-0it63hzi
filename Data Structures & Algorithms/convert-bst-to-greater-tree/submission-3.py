# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        vals = []
        q = deque([root])
        while q:
            node = q.popleft()      
            if not node:
                continue
            vals.append(node.val)
            q.append(node.left)
            q.append(node.right)

        vals.sort()
        vtoi = {v: i for i,v in enumerate(vals)}
        prefix = []
        acc = 0
        for v in vals:
            acc += v
            prefix.append(acc)

        print(vals)
        print(prefix)
        q = deque([root])
        while q:
            node = q.popleft()      
            if not node:
                continue
            node.val += acc - prefix[vtoi[node.val]] 
            vals.append(node.val)
            q.append(node.left)
            q.append(node.right)

        return root