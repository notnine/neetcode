class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1 for _ in range(n)]
        res = 1

        for i in range(n - 1, -1, -1):
            curr_num = nums[i]
            for j in range(i+1, n): # j iterates from "curr index" to the end
                if curr_num < nums[j]: # possible lis
                    memo[i] = max(memo[i], 1 + memo[j])
                    res = max(res, memo[i])
        
        return res