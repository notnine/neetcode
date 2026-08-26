class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # observation: if we skip a number, we must skip all of its instances
        nums.sort()
        res = []
        n = len(nums)

        def backtrack(curr: List[int], i: int) -> None:
            if i == n:
                res.append(curr.copy())
                return
            # take the number at i
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()
            # skip the number at i (and all its instances)
            while i + 1 < n and nums[i+1] == nums[i]:
                i += 1
            backtrack(curr, i + 1)
        
        backtrack([], 0)
        return res
        