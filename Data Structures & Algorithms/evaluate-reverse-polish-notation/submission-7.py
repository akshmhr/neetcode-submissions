import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
            }
        
        stack = []
        ans = 0
        for i in tokens:
            if i not in ops:
                stack.append(i)
                continue
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                ans = int(ops[i](b, a))
                stack.append(ans)

        return stack[-1]