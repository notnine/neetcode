class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        # dp[i] = # possible steps to i 
        # dp[i] = dp[i-1] + dp[i-2]
        # notice dp[i] only depends on the last 2 elements before it, so we actually only need to store 2 elements before it

        prev_2 = 1
        prev_1 = 2
        curr = 3

        for i in range(4, n + 1):
            temp = prev_1 + curr
            prev_2 = prev_1
            prev_1 = curr
            curr = temp
            print("i: " + str(i))
            print("prev_2: " + str(prev_2))
            print("prev_1: " + str(prev_1))
            print("curr: " + str(curr))
            print()

        return curr