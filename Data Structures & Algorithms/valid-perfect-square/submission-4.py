class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 2
        r = num // 2
        while l <= r:
            m = (r + l) // 2
            test = m*m
            if test > num:
                r = m - 1
            elif test < num:
                l = m + 1
            else:
                return True 
        return False
