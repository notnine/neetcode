class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        permutations = self.permute(nums[:])
        permutations.sort()
        for i, p in enumerate(permutations):
            if p == nums:
                nextP = permutations[(i + 1) % len(permutations)]
                for j in range(len(nums)):
                    nums[j] = nextP[j]
                break


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i):
            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1)

            for j in range(len(nums) - 1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]

        nums.sort()
        dfs(0)
        return res