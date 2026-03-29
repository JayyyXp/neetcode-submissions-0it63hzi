class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0
        T1 = 1
        T2 = 1

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        for i in range(2,n+1):
            new = T0 + T1 + T2 
            T0, T1, T2 = T1, T2, new
        return T1