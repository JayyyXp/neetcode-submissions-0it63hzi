class Solution:
    def reverse(self, x: int) -> int:
        listX = list(str(abs(x)))
        if len(listX) > 9:
            return 0
        listX.reverse()

        return int((''.join(listX))) if x > 0 else -1 * int((''.join(listX))) 