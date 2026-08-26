class Solution:
    def isValid(self, s: str) -> bool:
        opens = {'(','[','{'}
        stack = []

        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c == ')':
                    if top != '(':
                        return False
                if c == '}':
                    if top != '{':
                        return False
                if c == ']':
                    if top != '[':
                        return False
        
        return len(stack) == 0