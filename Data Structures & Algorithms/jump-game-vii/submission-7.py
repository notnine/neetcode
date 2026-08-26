class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [None] * n # dp[i] is True if can reach idx i
        dp[0] = True

        for i in range(1, n):
            # figure out if we can reach i
            if s[i] == '1':
                continue
            
            prev_range = [None, None]
            prev_range[0] = i - maxJump
            prev_range[1] = i - minJump

            print(prev_range)

            for prev_idx in range(prev_range[0], prev_range[1]+1):
                if 0 <= prev_idx < n and dp[prev_idx]:
                    dp[i] = True
                    break

        print(dp)
        return dp[n-1] if dp[n - 1] is not None else False