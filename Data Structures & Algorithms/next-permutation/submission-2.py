class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i) -> None:
            if i == len(nums):
                res.append(nums.copy())
                return

            seen = set()
            for j in range(i, len(nums)):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        perms = self.permute(nums)
        perms.sort()

        for i, perm in enumerate(perms):
            if perm == nums:
                next_perm_i = (i+1) % len(perms)
                break
        
        next_perm = perms[next_perm_i]
        for i in range(len(nums)):
            nums[i] = next_perm[i]
        