class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x *= -1
            is_negative = True
        
        x_str = list(str(x))
        res = int(''.join(x_str[::-1]))

        if is_negative:
            res *= -1

        if res < -2**31 or res > 2**31 -1:
            return 0

        return res