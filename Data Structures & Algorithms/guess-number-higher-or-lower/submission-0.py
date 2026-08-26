# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        curr = (1 + n) // 2
        l, r = 0, n

        while guess(curr) != 0:
            if guess(curr) == -1:
                r = curr - 1
            else:
                l = curr + 1
            curr = (l + r) // 2

        return curr