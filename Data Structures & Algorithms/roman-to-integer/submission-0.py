class Solution:
    def romanToInt(self, s: str) -> int:
        prev = None
        h = {
        "I":1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        ans = 0
        for c in s:
            if c == "V" and prev == "I":
                ans -= 1
                ans += 4
            elif c == "X" and prev == "I":
                ans -= 1
                ans += 9
            elif c == "L" and prev == "X":
                ans -= 10
                ans += 40
            elif c == "C" and prev == "X":
                ans -= 10
                ans += 90
            elif c == "D" and prev == "C":
                ans -= 100
                ans += 400
            elif c == "M" and prev == "C":
                ans -= 100
                ans += 900
            else:
                ans += h[c]
                prev = c
        return ans
                
