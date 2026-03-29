class CountSquares:

    def __init__(self):
        self.points = collections.defaultdict(int) # point (x,y) -> count

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1
        
    def count(self, point: List[int]) -> int:
        count = 0
        x0, y0 = point
        for (x1, y1), c in self.points.items():
            if x0 == x1 and y0 == y1:
                continue
            dx = x1 - x0
            dy = y1 - y0
            
            # Check if it forms a valid square (axis-aligned)
            if abs(dx) != abs(dy):
                continue
            count += self.points.get((x0, y1), 0) * self.points.get((x1, y0), 0) * c
        return count
 
                 