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
        import math
        from collections import defaultdict

        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False  # 1 can't connect to anything

        # Helper: prime factorization
        def get_prime_factors(x):
            factors = set()
            while x % 2 == 0:
                factors.add(2)
                x //= 2
            d = 3
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 2
            if x > 1:
                factors.add(x)
            return factors

        # Union numbers via shared primes
        prime_to_index = dict()
        dsu = DSU(n)

        for i, num in enumerate(nums):
            primes = get_prime_factors(num)
            for p in primes:
                if p in prime_to_index:
                    dsu.union(i, prime_to_index[p])
                else:
                    prime_to_index[p] = i

        # Check if all indices are in same DSU group
        return dsu.n == 1
