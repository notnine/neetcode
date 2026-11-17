class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # now xor is num1 ^ num2. Xor tells us where num1 and num2 differ. We can just take 1 of these bits where they differ, and from all the nums, we take the ones that have a 0, and the ones that have a 1. Then we xor the groups and we get back num1 and num2.

        # get least sig. 1 bit in xor.
        diff = 1
        while diff & xor == 0:
            diff = diff << 1
        
        zero_group = []
        one_group = []
        for num in nums:
            if num & diff != 0:
                one_group.append(num)
            else:
                zero_group.append(num)
        
        num1 = 0
        for num in zero_group:
            num1 ^= num
        num2 = 0
        for num in one_group:
            num2 ^= num
        return [num1, num2]