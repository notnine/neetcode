class Solution:
    def isHappy(self, n: int) -> bool:
        visitted = set()

        def recurse(curr: int) -> bool:
            if curr == 1:
                return True
            if curr in visitted:
                return False
            visitted.add(curr)
            curr_str = str(curr)
            sum_squares = 0
            for digit in curr_str:
                sum_squares += (int(digit) * int(digit))
            print(sum_squares)
            print()
            return recurse(sum_squares)

        return recurse(n)