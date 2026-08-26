# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of the max of the curr path so far
        res = 0

        def dfs(node: Optional[TreeNode], max_so_far: int) -> None:
            nonlocal res
            if not node:
                return
            
            if node and node.val >= max_so_far:
                res += 1
                max_so_far = node.val
            
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        
        dfs(root,-101)
        return res