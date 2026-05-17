class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # backtracking where we either place the flower at i or not

        # at pos i, return true if we can place left number of flowers
        def dfs(i: int, left: int) -> bool:
            if i >= len(flowerbed) and n > 0:
                return False
            if left == 0:
                return True

            # if we can place a flower here, place
            if flowerbed[i] == 0 and (
                    (i-1 >= 0 and flowerbed[i-1] == 0 and i+1 < len(flowerbed) and flowerbed[i+1] == 0) or (i == len(flowerbed) - 1 and i - 1 >= 0 and flowerbed[i-1] == 0) or (i == 0 and i + 1 < len(flowerbed) and flowerbed[i+1] == 0)
                    ):
                flowerbed[i] = 1
                left -= 1
                place = dfs(i + 1, left)
                if place:
                    return True
                flowerbed[i] = 0 # couldn't place so reset
                left += 1
        
            skip = dfs(i + 1, left)
            return skip
            

            


        return dfs(0, n)