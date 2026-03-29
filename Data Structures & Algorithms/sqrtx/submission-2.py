class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        print(13**0.5)
        print()

        diff = float('inf')
        i = 1
        while i <= x:
            if i*i == x:
                return i
            if i*i > x:
                return i-1

            i += 1 