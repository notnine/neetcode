class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charToFreq = defaultdict(int) # counter of curr window
        charToFreq[s[0]] = 1
        max_freq = 1 # max freq within window
        res = 0

        l, r = 0, 0
        while r < len(s):
            if (r - l + 1) - max_freq <= k:
                print("window size: " + str(r-l+1))
                print("max_freq: " + str(max_freq))
                print("charToFreq: " + str(charToFreq))
                print("curr VALID window: " + s[l:r + 1])
                res = max(res, r - l + 1)
                r += 1
                if r < len(s):
                    print("s[r]: " + str(s[r]))
                    charToFreq[s[r]] += 1
                    max_freq = max(max_freq, charToFreq[s[r]])
            else:
                print("window size: " + str(r-l+1))
                print("max_freq: " + str(max_freq))
                print("curr INVALID window: " + s[l:r + 1])
                charToFreq[s[l]] -= 1
                max_freq = max(charToFreq.values())
                l += 1
            print()
            

        return res

