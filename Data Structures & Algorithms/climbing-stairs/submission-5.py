class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [-1] * (n + 1)
        def counter(i):
            if i == 2:
                return 2
            if i == 1:
                return 1
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = counter(i-1) + counter(i-2)
            return cache[i]

        return counter(n)