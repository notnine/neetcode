class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # n candies among 3 children, where each child gets no more than limit candies
        res = 0 

        for c1 in range(limit+1):
            for c2 in range(limit+1):
                for c3 in range(limit+1):
                    if c1 + c2 + c3 == n:
                        res += 1
        
        return res