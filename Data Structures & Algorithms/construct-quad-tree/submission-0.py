"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS = len(grid)
        COLS = len(grid[0])
        has0, has1 = False, False 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    has0 = True
                else:
                    has1 = True
        if has0 and has1:
            rowHalf = ROWS // 2
            colHalf = COLS // 2
            topLeft = self.construct([row[:colHalf] for row in grid[:rowHalf]])
            topRight = self.construct([row[colHalf:] for row in grid[:rowHalf]])
            bottomLeft = self.construct([row[:colHalf] for row in grid[rowHalf:]])
            bottomRight = self.construct([row[colHalf:] for row in grid[rowHalf:]])
            return Node(-1, False, topLeft, topRight, bottomLeft, bottomRight)
        elif has0:
            return Node(0, True, None, None, None, None)
        else:
            return Node(1, True, None, None, None, None)