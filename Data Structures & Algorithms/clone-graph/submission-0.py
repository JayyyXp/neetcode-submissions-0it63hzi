"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def helper(node):
            if not node:
                return 
            if node in visited:
                return visited[node]
            new = Node(node.val)
            visited[node] = new
            new.neighbors = []
            for n in node.neighbors:
                new.neighbors.append(helper(n)) 
            
            return new
                
        return helper(node)