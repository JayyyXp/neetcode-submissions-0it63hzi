class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.n -= 1
        return True 
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        edges = [e + [i] for i, e in enumerate(edges)]
        edges.sort(key=lambda v: v[2])

        dsu = DSU(n)
        mst = 0
        for v1,v2,w,i in edges:
            if dsu.union(v1,v2):
                mst += w
        print(mst)
        crit = []
        pseudo = []
        for v1,v2,wi,i in edges:
            # crit
            dsu = DSU(n)
            newmst = 0
            for v1j,v2j,wj,j in edges:
                if i != j and dsu.union(v1j,v2j):
                    newmst += wj
            if dsu.n > 1 or newmst > mst:
                crit.append(i)
                continue
            
            # pseudo
            dsu = DSU(n)
            newmst = wi
            dsu.union(v1,v2)
            for v1j,v2j,wj,j in edges:
                if i != j and dsu.union(v1j,v2j):
                    newmst += wj
            if dsu.n == 1 and newmst == mst:
                pseudo.append(i)
        
        return [crit, pseudo]
            

        

