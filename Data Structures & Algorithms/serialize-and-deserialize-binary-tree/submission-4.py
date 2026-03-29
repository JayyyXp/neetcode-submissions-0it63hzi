# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    from collections import deque 

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""
        dq = deque([root])
        while dq:
            l = len(dq)
            for i in range(l):
                curr = dq.popleft()
                if not curr:
                    ans += 'N,'
                    continue
                ans += f"{str(curr.val)},"
                dq.append(curr.left)
                dq.append(curr.right)
        ans = ans[:-1]
        print(ans.split(","))
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 1:
            return None

        data = data.split(",")
        indexStart1 = 1
        root = TreeNode(val=int(data[0]))
        dq = deque([root])

        while indexStart1 != len(data):
            l = len(dq)
            print('child start', indexStart1, 'nodes in parent', l)
            for i in range(l):
                curr = dq.popleft()
                #if curr.val:
                if curr:
                    print(curr.val, data[indexStart1], data[indexStart1+1])
                    leftValue = None if data[indexStart1] == 'N' else int(data[indexStart1])
                    if leftValue: 
                        leftNode = TreeNode(val=leftValue)
                        curr.left = leftNode
                        dq.append(leftNode)
                    indexStart1 += 1

                    rightValue = None if data[indexStart1] == 'N' else int(data[indexStart1])
                    if rightValue:
                        rightNode = TreeNode(val=rightValue)
                        curr.right = rightNode
                        dq.append(rightNode)
                    indexStart1 += 1
                #else:
                #    indexStart1 += 1
            #indexStart1 += 1

        return root