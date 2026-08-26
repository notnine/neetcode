# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def get_gcd(num_1: int, num_2: int) -> int:
            # 0. set num_1 to be the smaller num
            if num_1 > num_2:
                num_1, num_2 = num_2, num_1

            # 1. return greatest common divisor, from num_1 to 1 inclusive
            for i in range(num_1, -1, -1):
                if num_1 % i == 0 and num_2 % i == 0:
                    return i


        prev = head
        curr = head.next

        while curr is not None:
            # 0. get gcd between prev & curr
            gcd = get_gcd(prev.val, curr.val)

            # 1. insert a new node b/w prev & curr of gcd
            new_node = ListNode(val=gcd, next=curr)
            prev.next = new_node

            # 2. update prev & curr
            prev = curr
            curr = prev.next

        return head