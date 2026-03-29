class DSU:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
    def find(self,x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.par[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.par[px] = py
        self.n -= 1
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        for i, (xi, yi) in enumerate(points):
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                edges.append(
                    [i,j,abs(xi - xj) + abs(yi - yj)]
                )
        edges.sort(key=lambda e: e[2])
        dsu = DSU(len(points))
        mst = 0
        for v1, v2, w in edges:
            if dsu.union(v1,v2):
                mst += w

        return mst