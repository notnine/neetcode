class Solution:
    def candy(self, ratings: List[int]) -> int:
        # approach 0: brute force
        n = len(ratings)
        res = [1] * n
        
        for i, r in enumerate(ratings):
            if i - 1 >= 0 and r > ratings[i-1]:
                res[i] = res[i-1] + 1
        
        for i in range(len(ratings) - 1, -1, -1):
            r = ratings[i]
            if i + 1 < n and r > ratings[i+1]:
                res[i] = res[i+1] + 1

        return sum(res)