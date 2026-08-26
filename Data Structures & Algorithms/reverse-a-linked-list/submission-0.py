# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        prev = None
        curr = head
        future = curr.next if curr else None

        # 1. point curr to prev
        # 2. update prev to become curr; curr to become next; next to become curr.next

        while future:
            curr.next = prev
            prev = curr
            curr = future
            future = curr.next
        
        curr.next = prev
        return curr