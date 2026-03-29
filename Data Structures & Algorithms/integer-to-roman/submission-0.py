class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []

        # thousands
        t = num // 1000
        ans.extend(["M"] * t)

        # hundreds
        h = (num % 1000) // 100
        if h < 4:
            ans.extend(["C"] * h)
        elif h == 9:
            ans.extend(["C", "M"])
        elif h == 4:
            ans.extend(["C", "D"])
        else:
            ans.append("D")
            ans.extend(["C"] * (h - 5))

        # tens
        tens = (num % 100) // 10
        if tens < 4:
            ans.extend(["X"] * tens)
        elif tens == 9:
            ans.extend(["X", "C"])
        elif tens == 4:
            ans.extend(["X", "L"])
        else:
            ans.append("L")
            ans.extend(["X"] * (tens - 5))

        # ones
        o = num % 10
        if o < 4:
            ans.extend(["I"] * o)
        elif o == 9:
            ans.extend(["I", "X"])
        elif o == 4:
            ans.extend(["I", "V"])
        else:
            ans.append("V")
            ans.extend(["I"] * (o - 5))

        return "".join(ans)
