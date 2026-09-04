class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # n candies among 3 children, where each child gets no more than limit candies
        res = 0 

        for c1 in range(limit+1):
            for c2 in range(limit+1):
                c3 = n - c1 - c2
                if 0 <= c3 <= limit:
                    res += 1
        
        return res