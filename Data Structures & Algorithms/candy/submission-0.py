class Solution:
    def candy(self, ratings: List[int]) -> int:
        # approach 0: brute force
        n = len(ratings)
        res = [1] * n
        
        for i, r in enumerate(ratings):
            # if prev neighbor's rating is higher than curr rating
            if i - 1 >= 0 and ratings[i-1] > r:
                # add 1 to prev nei & propogate backwards
                j = i - 1
                while j >= 0 and ratings[j+1] < ratings[j]:
                    res[j] = res[j+1] + 1
                    j -= 1
        
        for i in range(len(ratings) - 1, -1, -1):
            r = ratings[i]
            # if prev neighbor's rating is higher than curr rating
            if i + 1 < n and ratings[i+1] > r:
                # add 1 to prev nei & propogate backwards
                j = i + 1
                while j < n and ratings[j-1] < ratings[j]:
                    res[j] = res[j-1] + 1
                    j += 1

        print(res)
        return sum(res)