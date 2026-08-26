class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n):

                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                l, r = j + 1, n - 1
                t = target - (nums[i] + nums[j])

                if nums[i] == -3 and nums[j] == -1:
                    print(t)

                while l < r:
                    
                    curr = nums[l] + nums[r]
                    if curr > t:
                        r -= 1
                    elif curr < t:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1

                        while l < r and nums[l-1] == nums[l]:
                            l += 1
        
        return res

                    

