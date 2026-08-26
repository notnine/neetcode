from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def dfs():
            print(tokens)
            print()
            token = tokens.pop()
            if token not in '+-*/':
                return int(token)
            
            r = dfs()
            l = dfs()

            if token == '+':
                return l + r
            elif token == '-':
                return l - r
            elif token == '*':
                return l * r
            else:
                return int(l / r)
            
        return dfs()