class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0 for _ in range(n + 1)]

        for i in range(n+1):
            curr_ones = 0
            curr_num = i
            while curr_num:
                if curr_num & 1:
                    curr_ones += 1
                curr_num >>= 1
            res[i] = curr_ones
        
        return res