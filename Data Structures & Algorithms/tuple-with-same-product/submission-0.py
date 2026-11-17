from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        product_pair_count = defaultdict(int)
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_pair_count[product] += product_count[product]
                product_count[product] += 1
        
        res = 0
        for product in product_pair_count:
            res += product_pair_count[product] * 8
        
        return res
