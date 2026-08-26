class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [None] * n # dp[i] is True if can reach idx i
        dp[0] = True
        reachables = 0

        for i in range(1, n):

            # if window's old left border was reachable
            if 0 <= i - maxJump - 1 < n and dp[i - maxJump - 1] is True:
                print(i - maxJump - 1)
                reachables -= 1
            
            # if window's new right border is reachable
            if 0 <= i - minJump < n and dp[i - minJump] is True:
                reachables += 1
            
            # then i is reachable at this point
            if reachables > 0 and s[i] == '0':
                dp[i] = True
        
        print()
        print(dp)
        return dp[n - 1] if dp[n - 1] else False