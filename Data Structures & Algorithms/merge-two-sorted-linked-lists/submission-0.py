# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        curr = ListNode(val=-2,next=None)
        prev_head = ListNode(val=-1,next=None)

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
            if not prev_head.next:
                prev_head.next = curr

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return prev_head.next
            
