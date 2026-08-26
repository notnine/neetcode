class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1 for _ in range(len(nums))]
        postfix_products = [1 for _ in range(len(nums))]

        prefix_product = 1
        for i in range(len(nums)):
            prefix_products[i] = prefix_product
            prefix_product *= nums[i]
        
        postfix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_products[i] = postfix_product
            postfix_product *= nums[i]
        
        print("prefix products: " + str(prefix_products))
        print("postfix products: " + str(postfix_products))

        res = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            res[i] = prefix_products[i] * postfix_products[i]
        
        return res