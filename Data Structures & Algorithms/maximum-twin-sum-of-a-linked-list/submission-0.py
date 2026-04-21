# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # reverse 2nd half. do a fast & slow pointer to get slow ptr to start of 2nd half
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        # reverse slow onwards
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            curr, prev = next_temp, curr
        
        # now prev is at head of reversed second half
        res = 0
        forward, backward = head, prev
        while backward:
            res = max(res, forward.val + backward.val)
            forward = forward.next
            backward = backward.next
        
        return res
