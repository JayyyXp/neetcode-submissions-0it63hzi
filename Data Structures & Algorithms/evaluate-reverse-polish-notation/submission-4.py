class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in range(len(tokens)):
            
            operand = tokens[i]
            print(stack, operand)
            if operand == "+":
                sec = stack.pop()
                fir = stack.pop()
                stack.append(
                    fir + sec
                )
            elif operand == "-":
                sec = stack.pop()
                fir = stack.pop()
                stack.append(
                    fir - sec
                )            
            elif operand == "*":
                sec = stack.pop()
                fir = stack.pop()
                stack.append(
                    fir * sec
                )
            elif operand == "/":
                sec = stack.pop()
                fir = stack.pop()
                stack.append(
                    int(float(fir) / sec)
                )
            else:
                stack.append(int(operand))
            
        return stack[0]