class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                print(stack, c)
                if not stack:
                    return False
                last = stack.pop()
                if last == "(" and c == ")":
                    continue
                elif last == "{" and c == "}":
                    continue
                elif last == "[" and c == "]":
                    continue
                else:
                    return False
        
        return not stack
