# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and subRoot:
            return False
        if not root and not subRoot:
            return True

        def isSameTree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if not node1 and not node2:
                return True
            if not node1 and node2 or not node2 and node1:
                return False
            if node1.val != node2.val:
                return False
            return isSameTree(node1.left, node2.left) and isSameTree(node1.right, node2.right)

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)