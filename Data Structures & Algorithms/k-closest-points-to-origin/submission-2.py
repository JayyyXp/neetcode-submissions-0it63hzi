class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distToPoint = [ 
            [pow(x,2) + pow(y,2), x, y]
            for x, y in points 
        ]
        print(distToPoint)
        #distToPoint = sorted(distToPoint)
        #return [distToPoint[i][1] for i in range(k)]
        heapq.heapify(distToPoint)
        ans = []
        while k > 0:
            el = heapq.heappop(distToPoint)
            ans.append(el[1:])
            k -= 1
        return ans