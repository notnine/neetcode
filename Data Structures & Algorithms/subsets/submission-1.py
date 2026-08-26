class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, curr: List[int]):
            if i >= len(nums):
                res.append(curr.copy())
                return
            
            # do not take curr element
            backtrack(i + 1, curr)
            # take curr element
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

        backtrack(0, [])
        return res
