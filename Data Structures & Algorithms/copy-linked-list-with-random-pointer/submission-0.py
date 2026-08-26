"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {}

        # create new copies of nodes
        curr = head
        while curr:
            new = Node(curr.val)
            oldToNew[curr] = new
            curr = curr.next
        
        # update the next and random attributes of the new copies
        curr = head
        while curr:
            new = oldToNew[curr]
            new.next = oldToNew[curr.next] if curr.next else None
            new.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        
        return oldToNew[head] if head else None