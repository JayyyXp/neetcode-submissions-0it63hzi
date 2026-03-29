class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            ans = 1 / x
            for i in range(1,abs(n)):
                ans *= (1 / x)
        else:
            ans = x
            for i in range(1,abs(n)):
                ans *= x
        
        return ans