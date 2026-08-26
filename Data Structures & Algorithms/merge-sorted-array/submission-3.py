class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = (m + n) - 1
        n1_ptr = m - 1
        n2_ptr = n - 1

        while curr >= 0:
            if n1_ptr == -1: # if we finished nums1, put nums2 remaining items in the front
                for i in range(n2_ptr, -1, -1):
                    nums1[i] = nums2[n2_ptr]
                    n2_ptr -= 1
                return
            if n2_ptr == -1:
                print(nums1)
                for i in range(n1_ptr, -1, -1): # do we actually have to do this
                    nums1[i] = nums1[n1_ptr]
                    n1_ptr -= 1
                return
                        
            if nums1[n1_ptr] >= nums2[n2_ptr]:
                nums1[curr] = nums1[n1_ptr]
                n1_ptr -= 1
            else:
                nums1[curr] = nums2[n2_ptr]
                n2_ptr -= 1
            curr -= 1
        