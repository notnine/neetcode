class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n, m = len(s1), len(s2)
        window = defaultdict(int) # Counter for window
        s1_counter = defaultdict(int)

        # initialize window counter
        for i in range(n):
            window[s2[i]] += 1
            s1_counter[s1[i]] += 1

        l, r = 0, n - 1
        while (r + 1) < m:
            if window == s1_counter:
                return True
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            window[s2[r+1]] += 1
            l, r = l + 1, r + 1

        # check last possible window (since we skipped it in the loop)
        if window == s1_counter:
            return True
        
        return False
