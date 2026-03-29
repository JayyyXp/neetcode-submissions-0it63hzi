class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = 0
        carry = 0
        for i in range(32):
            ai =  (a >> i) & 1
            bi =  (b >> i) & 1
            if ai & bi & carry:
                ans = ans | (1 << i)
                carry = 1
            elif ai & bi and not carry:
                carry = 1
            elif ai ^ bi and not carry:
                ans = ans | (1 << i)
            elif ai ^ bi and carry:
                carry = 1
            elif not ai and not bi and carry:
                ans = ans | (1 << i)
                carry = 0
        mask = 0xFFFFFFFF
        if ans > 0x7FFFFFFF:
            ans = ~(ans ^ mask)
            
        return ans