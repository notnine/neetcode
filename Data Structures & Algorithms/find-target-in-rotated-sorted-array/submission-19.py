class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            print(nums[l:r+1])
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: # left part is sorted 
                if nums[l] <= target < nums[m]: # search in left (sorted) part
                    print("A")
                    r = m - 1
                else:
                    print("B")
                    l = m + 1

            else: # right part is sorted
                if nums[m] < target <= nums[r]: # search in right (sorted) part
                    print("C")
                    l = m + 1
                else: 
                    print("D")
                    r = m - 1

            print()

        return -1