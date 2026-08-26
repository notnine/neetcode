# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = [] # vals in in-order traversal. k'th smallest is at index k

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return vals[k-1]