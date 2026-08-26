# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
        # 2 pointers, 1 at head, 1 at head + n. therfore, first ptr is n behind.

        slow = head
        prev = ListNode(val=99,next=slow)
        n_ahead = head

        # [1,2]
        # 2

        for i in range(n):
            if n_ahead.next:
                n_ahead = n_ahead.next
            else:
                if i == (n-1):
                    return head.next
                else:
                    return None
        
        print(n_ahead.val)

        while n_ahead:
            slow = slow.next
            prev = prev.next
            n_ahead = n_ahead.next
        
        # now n_ahead is at the end, so slow is the node to be popped
        prev.next = slow.next
        return head
