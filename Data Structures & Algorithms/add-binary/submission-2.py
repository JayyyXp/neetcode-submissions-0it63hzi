class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        la = len(a)
        lb = len(b)
        if la > lb:
            b = (la - lb) * "0" + b
        elif lb > la:
            a = (lb - la) * "0" + a
        carry = 0
        for a1, b1 in zip(reversed(a),reversed(b)):
            c = int(a1) + int(b1) + carry
            if c == 3:
                carry = 1
                ans = "1" + ans
            elif c == 2:
                carry = 1
                ans = "0" + ans
            elif c == 1:
                carry = 0
                ans = "1" + ans
            elif c == 0:
                carry = 0
                ans = "0" + ans
        if carry == 1:
            ans = "1" + ans
        return ans