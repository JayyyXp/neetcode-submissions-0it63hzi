class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            for i in range(len(row)-1):
                row[i].next = row[i+1]
        return root