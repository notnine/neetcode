class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # aproach 1: start with bin(x). We basically want to take the 0 bits, and count up to n-1. So just embed n-1 into bin x's 0 bits.

        # get bin(x) and bin(n-1)
        x_bin = [0] * 64
        n_bin = [0] * 64 # bin rep of n-1
        n -= 1
        ori_x, ori_n = x, n

        for i in range(32):
            x_bin[i] = x & 1
            n_bin[i] = n & 1
            x = x >> 1
            n = n >> 1

        # embed n-1 into the 0 bits of x
        n, x = ori_n, ori_x
        i = 0
        while i < 64:
            while i < 64 and x_bin[i] == 1:
                i += 1
            x_bin[i] = n & 1
            n = n >> 1
            i += 1

        # return int
        res = 0
        for i in range(64):
            res += 2 ** i if x_bin[i] == 1 else 0

        return res        

