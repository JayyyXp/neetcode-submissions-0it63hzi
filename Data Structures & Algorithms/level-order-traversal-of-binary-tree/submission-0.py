# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque 

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        def bfs(node):

            deq = deque([node])  
            while deq:
                n = len(deq)
                temp = []
                #print(deq)
                for i in range(n):
                    curr = deq.popleft()
                    if not curr:
                        continue
                    
                    temp.append(curr.val)
                    deq.append(curr.left)
                    deq.append(curr.right)
                if temp:
                    ans.append(temp)


        bfs(root)
        return ans