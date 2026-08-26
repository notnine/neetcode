# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root: Optional[TreeNode], pathMin: int, pathMax: max) -> None:
            if not root: 
                return True

            if not (pathMin < root.val < pathMax):
                return False
            
            return valid(root.left, pathMin, root.val) and valid(root.right, root.val, pathMax)

        return valid(root, -1001, 1001)