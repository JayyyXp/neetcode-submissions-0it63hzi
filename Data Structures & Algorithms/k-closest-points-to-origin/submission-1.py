class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distToPoint = [ 
            (math.sqrt(pow(point[0],2) + pow(point[1],2)), point)
            for point in points 
        ]
        print(distToPoint)
        distToPoint = sorted(distToPoint)
        print(distToPoint)

        return [distToPoint[i][1] for i in range(k)]