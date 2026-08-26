class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = 0, 0

        for i in range(len(s)):
            print("Ï: " + str(i))
            # check for even-length palis
            l, r = i, i + 1
            # check longest possible pali with l, r as "mid" points
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l -= 1
                r += 1
            # udpate reses
            l, r = l + 1, r - 1
            if (r - l + 1) > resLen:
                resLen = (r - l + 1)
                res = l
            l, r = i - 1, i + 1
            # check for odd-length palis
            # check longest possible pali with l+1 as "mid" point
            while 0 <= l < len(s) and 0 <= r < len(s) and s[l:r+1] == s[l:r+1][::-1]:
                l -= 1
                r += 1
            l, r = l + 1, r - 1
            if (r - l + 1) > resLen:
                resLen = (r - l + 1)
                res = l
        print("res: "+str(res))
        print("resLen: "+str(resLen))
        return s[res:res+resLen]