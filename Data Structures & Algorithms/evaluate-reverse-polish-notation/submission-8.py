import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                stack.append(int(i))
                continue
            else:
                a = stack.pop()
                b = stack.pop()

                ans = int(ops[i](b, a))
                stack.append(ans)

        return stack[-1]