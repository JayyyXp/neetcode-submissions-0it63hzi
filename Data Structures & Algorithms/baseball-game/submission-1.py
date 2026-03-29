class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == "+":
                total += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                total += stack[-1] *2
                stack.append(stack[-1] *2)
            elif op == "C":
                el =stack.pop()
                total -= el
            else:
                stack.append(int(op))
                total += int(op)
        return total #sum(stack)