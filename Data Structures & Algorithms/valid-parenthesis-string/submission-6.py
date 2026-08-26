class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy
        # keep track of possible num of min opens and max opens

        min_opens, max_opens = 0, 0

        for c in s:
            if c == '(':
                min_opens += 1
                max_opens += 1
            elif c == ')':
                min_opens = max(min_opens - 1, 0)
                max_opens -= 1
            else:
                min_opens = max(min_opens - 1, 0)
                max_opens += 1
            if max_opens < 0:
                return False
        
        return min_opens == 0