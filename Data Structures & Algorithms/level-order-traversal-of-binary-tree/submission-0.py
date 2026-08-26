# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr = deque([root])
        res = [[root.val]]

        while curr:
            next_lvl = []
            while curr:
                curr_node = curr.popleft()
                if curr_node.left:
                    next_lvl.append(curr_node.left) 
                if curr_node.right:
                    next_lvl.append(curr_node.right)
            if next_lvl:
                res.append([node.val for node in next_lvl])
            curr = deque(next_lvl)
        
        return res
