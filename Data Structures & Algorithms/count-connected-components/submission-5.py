class DSU:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))
        self.n = n

    def find(self, x):
        px = self.parent[x]
        if px != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[px]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return 

        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.parent[py] = px
        else: 
            self.rank[py] += self.rank[px]
            self.parent[px] = py
        self.n -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        for a, b in edges:
            dsu.union(a, b)

        return dsu.n