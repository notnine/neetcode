# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:    
        if not root:
            return []

        curr_lvl = deque([root])
        res = [root.val]

        while len(curr_lvl) > 0:
            next_lvl = deque([])
            print(curr_lvl)
            print()
            curr_node = curr_lvl.popleft() if curr_lvl else None
            while curr_node is not None:
                if curr_node.left is not None:
                    next_lvl.append(curr_node.left)
                if curr_node.right is not None:
                    next_lvl.append(curr_node.right)
                curr_node = curr_lvl.popleft() if curr_lvl else None
            # curr_lvl's empty
            if next_lvl:
                res.append(next_lvl[-1].val)
            curr_lvl = next_lvl
        
        return res