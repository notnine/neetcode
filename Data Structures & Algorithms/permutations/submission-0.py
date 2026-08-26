class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        perms = self.permute(nums[1:])
        last = nums[0]
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                copy = perm.copy()
                copy.insert(i, last)
                res.append(copy)

        return res