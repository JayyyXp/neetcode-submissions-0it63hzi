class Solution:
    def calculate(self, s: str) -> int:
        
        def listToNum(l):
            acc = 0
            for n in num:
                acc += n
                acc *= 10
            return acc // 10
        helper = []
        num = []
        ev = False
        for c in s:
            # 10 * 10 +
            if c in ['+', '-', '*', '/']:
                num2 = listToNum(num)
                if ev:
                    op = helper.pop()
                    num1 = helper.pop()
                    if op == "*":
                        helper.append(num1*num2)
                    else:
                        helper.append(num1//num2)                    
                else:
                    helper.append(num2)
                ev = c in ['*', '/'] 
                helper.append(c)
                num = []
            elif c == " ":
                continue
            else:
                num.append(int(c))
        
        num2 = listToNum(num)
        if ev:
            op = helper.pop()
            num1 = helper.pop()
            if op == "*":
                helper.append(num1*num2)
            else:
                helper.append(num1//num2)                    
        else:
            helper.append(num2)

        print(helper)        

        ans = 0
        op = "+"
        for num in helper:
            if num not in ["+", "-"]:
                if op == "+":
                    ans += num
                else:
                    ans -= num
            else:
                op = num
        return ans