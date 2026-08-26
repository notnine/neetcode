class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # only contains open brackets
        open_brackets = set(['(','{','['])
        closed_to_open = {']':'[',')':'(','}':'{'}

        # stack: ,
        # top: [
        # c: ]

        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if closed_to_open[c] != top:
                    return False

        return True if not stack else False
        # {}[]()