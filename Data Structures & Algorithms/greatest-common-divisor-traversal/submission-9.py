class DSU:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.par[px] = py
            self.rank[py] += self.rank[px]
        self.n -= 1
        return True
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        def primeFactors(x):
            factors = set()
            f = 2
            while f * f <= x:
                while x % f == 0:
                    factors.add(f)
                    x //= f
                f += 1
            if x > 1:
                factors.add(x)
            return factors
        dsu = DSU(len(nums))
        prime_to_index = dict()

        for i, n in enumerate(nums):
            factors = primeFactors(n)
            for f in factors:
                if f in prime_to_index:
                    dsu.union(i,prime_to_index[f])
                else:
                    prime_to_index[f] = i
        # Check if all indices are in same DSU group
        return dsu.n == 1

