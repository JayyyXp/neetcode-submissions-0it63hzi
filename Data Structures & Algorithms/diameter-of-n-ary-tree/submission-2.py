"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        

        def dfs(node):
            if not node:
                return 0,0 # local ans, max path
            max_paths = [0,0]
            max_local = 0 
            for child in node.children:
                local_ans, max_path = dfs(child)
                max_local = max(max_local, local_ans)
                max_path += 1

                max_paths.append(max_path)
                max_paths.sort()
                max_paths = max_paths[1:]
                print(max_paths)
                
            new_local = max(max_local, sum(max_paths))

            return new_local, max(max_paths)

        return dfs(root)[0]