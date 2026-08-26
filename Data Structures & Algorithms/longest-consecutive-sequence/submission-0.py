class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr = 1
                up = num + 1
                while up in num_set:
                    curr += 1
                    up += 1
                res = max(res, curr)
        
        return res