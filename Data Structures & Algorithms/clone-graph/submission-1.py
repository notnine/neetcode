"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        visitted = set()
        oldToNew = {}

        def cloneNode(old: 'Node') -> 'Node':
            if old in visitted:
                return oldToNew[old]
            new = Node(val=old.val)
            visitted.add(old)
            oldToNew[old] = new
            for old_nei in old.neighbors:
                if old_nei in visitted:
                    new.neighbors.append(oldToNew[old_nei])
                else:
                    new.neighbors.append(cloneNode(old_nei))
            return new
        
        return cloneNode(node)