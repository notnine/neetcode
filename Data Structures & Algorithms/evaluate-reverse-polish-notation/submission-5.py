from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = '+-*/'
        curr = []

        def calc(op: str) -> None:
            nonlocal curr
            n1 = int(curr.pop())
            n2 = int(curr.pop())
            if op == '+':
                res = n2 + n1
            elif op == '-':
                res = n2 - n1
            elif op == '*':
                res = n2 * n1
            else:
                res = int(n2 / n1)
            curr.append(str(res))

        for t in tokens:
            if t not in ops:
                curr.append(t)
            else:
                calc(t)

        return int(curr[-1])