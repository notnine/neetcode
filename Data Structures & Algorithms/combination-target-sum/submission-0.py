class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i: int, total: int) -> None:
            if (i >= len(nums) and total != target) or (total > target):
                return
            if (target == total):
                res.append(curr.copy())
                return
            # take curr number
            curr.append(nums[i])
            backtrack(i, total + nums[i])
            curr.pop()
            # skip curr number
            backtrack(i+1,total)
        
        backtrack(0,0)
        return res
